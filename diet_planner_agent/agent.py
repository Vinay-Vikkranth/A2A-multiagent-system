import logging
import os

from collections.abc import AsyncIterable
from typing import Any, Literal

import httpx

from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_vertexai import ChatVertexAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


memory = MemorySaver()

# diet plan tool
@tool
def get_diet_plan(
    age: int,
    gender: str = 'unspecified',
    dietary_goal: str = 'general health',
    dietary_preference: str = 'none',
):
    """Suggest a simple personalized diet plan based on user input.

    Args:
        age: Age of the user.
        gender: Gender of the user (e.g., 'male', 'female', 'unspecified').
        dietary_goal: The user's dietary goal (e.g., 'weight loss', 'muscle gain', 'general health').
        dietary_preference: Dietary preference (e.g., 'vegetarian', 'vegan', 'none').

    Returns:
        A dictionary containing a sample diet plan.
    """
    # Example logic for demonstration
    plan = {
        'breakfast': 'Oatmeal with fruits and nuts',
        'lunch': 'Grilled chicken salad with mixed greens',
        'dinner': 'Baked salmon with steamed vegetables',
        'snacks': 'Greek yogurt, mixed berries, or nuts',
        'note': 'Drink plenty of water throughout the day.'
    }
    if dietary_preference.lower() == 'vegetarian':
        plan['lunch'] = 'Chickpea salad with mixed greens'
        plan['dinner'] = 'Lentil curry with brown rice'
    elif dietary_preference.lower() == 'vegan':
        plan['breakfast'] = 'Chia pudding with almond milk and fruits'
        plan['lunch'] = 'Quinoa salad with beans and veggies'
        plan['dinner'] = 'Stir-fried tofu with vegetables and brown rice'
    if dietary_goal.lower() == 'weight loss':
        plan['note'] += ' Focus on portion control and avoid sugary drinks.'
    elif dietary_goal.lower() == 'muscle gain':
        plan['note'] += ' Include a source of protein with every meal.'
    return {
        'age': age,
        'gender': gender,
        'dietary_goal': dietary_goal,
        'dietary_preference': dietary_preference,
        'diet_plan': plan
    }

# Response format for the agent's output
class ResponseFormat(BaseModel):
    status: Literal['input_required', 'completed', 'error'] = 'input_required'
    message: str

# Diet Planner Agent
class DietPlannerAgent:
    """DietPlannerAgent - a specialized assistant for diet planning."""

    SYSTEM_INSTRUCTION = (
        'You are a specialized assistant for providing personalized diet plans and nutrition advice. '
        'Your sole purpose is to suggest healthy meal plans, dietary recommendations, and answer questions related to nutrition and healthy eating. '
        'If the user asks about anything other than diet, nutrition, or meal planning, '
        'politely state that you cannot help with that topic and can only assist with diet and nutrition-related queries. '
        'Do not attempt to answer unrelated questions or use tools for other purposes.'
    )

    FORMAT_INSTRUCTION = (
        'Set response status to input_required if the user needs to provide more information to complete the request.'
        'Set response status to error if there is an error while processing the request.'
        'Set response status to completed if the request is complete.'
    )

    def __init__(self):
        model_source = os.getenv('model_source', 'google')
        if model_source == 'google':
            if os.getenv('GOOGLE_GENAI_USE_VERTEXAI', 'FALSE').upper() == 'TRUE':
                self.model = ChatVertexAI(
                    model='gemini-2.5-flash',  # or another Vertex AI model name
                    project=os.getenv('GOOGLE_CLOUD_PROJECT'),
                    location=os.getenv('GOOGLE_CLOUD_LOCATION'),
                )
            else:
                self.model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
        self.tools = [get_diet_plan]  
        # creating graph for the agent
        self.graph = create_react_agent(
            self.model,
            tools=self.tools,
            checkpointer=memory,
            prompt=self.SYSTEM_INSTRUCTION,
            response_format=(self.FORMAT_INSTRUCTION, ResponseFormat),
        )

    async def stream(self, query, context_id) -> AsyncIterable[dict[str, Any]]:
        inputs = {'messages': [('user', query)]}
        config = {'configurable': {'thread_id': context_id}}

        for item in self.graph.stream(inputs, config, stream_mode='values'):
            message = item['messages'][-1]
            if (
                isinstance(message, AIMessage)
                and message.tool_calls
                and len(message.tool_calls) > 0
            ):
                yield {
                    'is_task_complete': False,
                    'require_user_input': False,
                    'content': 'Looking up the diet...',
                }
            elif isinstance(message, ToolMessage):
                yield {
                    'is_task_complete': False,
                    'require_user_input': False,
                    'content': 'Processing the diet...',
                }
        # test
        logger.info('STREAMING COMPLETED')
        yield self.get_agent_response(config)

    def get_agent_response(self, config):
        current_state = self.graph.get_state(config)
        structured_response = current_state.values.get('structured_response')
        if structured_response and isinstance(
            structured_response, ResponseFormat
        ):
            if structured_response.status == 'input_required':
                return {
                    'is_task_complete': False,
                    'require_user_input': True,
                    'content': structured_response.message,
                }
            if structured_response.status == 'error':
                return {
                    'is_task_complete': False,
                    'require_user_input': True,
                    'content': structured_response.message,
                }
            if structured_response.status == 'completed':
                return {
                    'is_task_complete': True,
                    'require_user_input': False,
                    'content': structured_response.message,
                }

        return {
            'is_task_complete': False,
            'require_user_input': True,
            'content': (
                'We are unable to process your request at the moment. '
                'Please try again.'
            ),
        }

    SUPPORTED_CONTENT_TYPES = ['text', 'text/plain']

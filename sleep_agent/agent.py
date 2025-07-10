from google.adk.agents import Agent
from google.adk.tools import google_search


root_agent = Agent(
    name="sleep_agent",
    model="gemini-2.5-flash",
    description=("Agent to tell the required sleep hours"),
    instruction=("You are a helpful agent who can provide sleep hour recommendations by analyzing the user's input."),
    tools=[google_search],
)

import logging

import click
import uvicorn

from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
)

from health_care_multiagent.sleep_agent.agent import root_agent as sleep_agent
from health_care_multiagent.sleep_agent.agent_executor import ADKAgentExecutor
from dotenv import load_dotenv


load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MissingAPIKeyError(Exception):
    """Exception for missing API key."""


@click.command()
@click.option("--host", default="localhost")
@click.option("--port", default=10011)
def main(host, port):
    # Agent card (metadata)
    agent_card = AgentCard(
        name=sleep_agent.name,
        description=sleep_agent.description,
        url=f'http://{host}:{port}/',
        version="1.0.0",
        defaultInputModes=["text", "text/plain"],
        defaultOutputModes=["text", "text/plain"],
        capabilities=AgentCapabilities(streaming=True),
        skills=[
            AgentSkill(
                id="give_sleep_hours",
                name="Provide Sleep Hours",
                description="Searches Google for sleep hour recommendations.",
                tags=["search", "google", "sleep"],
                examples=[
                    "How many hours of sleep do I need?",
                    "What are the recommended sleep hours for adults?",
                ],
            )
        ],
    )

    request_handler = DefaultRequestHandler(
        agent_executor=ADKAgentExecutor(
            agent=sleep_agent,
        ),
        task_store=InMemoryTaskStore(),
    )

    server = A2AStarletteApplication(
        agent_card=agent_card, http_handler=request_handler
    )

    uvicorn.run(server.build(), host=host, port=port)


if __name__ == "__main__":
    main()

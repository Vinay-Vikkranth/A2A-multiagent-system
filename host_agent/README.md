# Host Agent

## Overview
The Host Agent acts as the central coordinator in a multi-agent health care system. It manages communication between specialized agents (such as sleep and diet planner agents), routes user queries to the appropriate agent, and aggregates responses to provide a seamless user experience.

## Features
- Routes user queries to the correct specialized agent (e.g., sleep, diet planner).
- Manages remote agent connections and communication.
- Aggregates and returns responses from multiple agents.
- Designed for extensibility and integration with additional health care agents.

## Usage
The Host Agent is intended to be the entry point for user interactions in the health care multi-agent system. It can:
- Receive user queries on various health topics.
- Determine which agent(s) should handle the query.
- Collect and return responses from the relevant agent(s).

## How It Works
- The Host Agent receives a user query.
- It analyzes the query and determines the appropriate agent(s) to handle it.
- It forwards the query, manages communication, and returns the aggregated response.

## Configuration
- **Name:** host_agent
- **Description:** Central coordinator for routing and managing health care agents
- **Instruction:** Receives user queries, routes them to the appropriate agent, and returns the response.
- **Tools:** Remote agent connection, routing logic

## Requirements
- Python 3.8+
- Dependencies as specified in the parent project's `requirements.txt`

## File Structure
- `__main__.py`: Entry point for running the host agent as a standalone module.
- `remote_agent_connection.py`: Handles connections to remote agents.
- `routing_agent.py`: Contains logic for routing queries to the correct agent.
- `README.md`: This file.
- `static/`: Contains static assets (e.g., images).

## How to Run

You can run the Host Agent as a standalone module using the following command from the `host_agent` directory:

```
python -m host_agent
```

Make sure all dependencies are installed and you are in the correct environment. For example:

1. Install dependencies (from the project root):
   ```
   pip install -r requirements.txt
   ```
2. Navigate to the `host_agent` directory:
   ```
   cd health_care_multiagent/host_agent
   ```
3. Run the agent:
   ```
   python -m host_agent
   ```

The agent will start and be ready to coordinate queries between specialized agents.

## Example
```
User: What is a good sleep schedule for a 30-year-old?
Host Agent: [Routes query to Sleep Agent and returns the response.]
```

## License
See the main project for license information.

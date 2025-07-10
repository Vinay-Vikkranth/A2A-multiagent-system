# Sleep Agent

## How to Run

You can run the Sleep Agent as a standalone module using the following command from the `sleep_agent` directory:

```
python -m sleep_agent
```

Make sure all dependencies are installed and you are in the correct environment. For example:

1. Install dependencies (from the project root):
   ```
   pip install -r requirements.txt
   ```
2. Navigate to the `sleep_agent` directory:
   ```
   cd health_care_multiagent/sleep_agent
   ```
3. Run the agent:
   ```
   python -m sleep_agent
   ```

The agent will start and be ready to receive queries about sleep recommendations.

## Overview
The Sleep Agent is an intelligent agent designed to provide personalized sleep hour recommendations based on user input. It leverages advanced language models and integrates with Google Search to deliver accurate and helpful advice regarding sleep requirements.

## Features
- Analyzes user input to recommend optimal sleep hours.
- Utilizes the Gemini 2.5 Flash model for natural language understanding.
- Integrates with Google Search for up-to-date information.
- Designed to be a helpful assistant for health and wellness applications.

## Usage
This agent is intended to be used as part of a multi-agent health care system. It can be invoked to answer questions such as:
- "How many hours should I sleep if I am 25 years old?"
- "What are the recommended sleep hours for teenagers?"
- "How does sleep requirement change with age?"

## How It Works
- The agent receives user queries related to sleep.
- It analyzes the input and, if necessary, uses Google Search to supplement its knowledge.
- It responds with a recommendation or relevant information about sleep hours.

## Configuration
- **Name:** sleep_agent
- **Model:** gemini-2.5-flash
- **Description:** Agent to tell the required sleep hours
- **Instruction:** Provides sleep hour recommendations by analyzing user input.
- **Tools:** Google Search

## Requirements
- Python 3.8+
- Dependencies as specified in the parent project's `requirements.txt`
- Access to the Google ADK and Gemini models

## File Structure
- `agent.py`: Main agent definition and configuration.
- `agent_executor.py`: (If present) Handles agent execution logic.
- `__main__.py`: Entry point for running the agent as a standalone module.

## Example
```
User: How many hours should a 16-year-old sleep?
Sleep Agent: Teenagers (14-17 years) are recommended to get 8-10 hours of sleep per night.
```

## License
See the main project for license information.

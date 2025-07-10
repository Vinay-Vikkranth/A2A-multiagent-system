# Diet Planner Agent

## Overview
The Diet Planner Agent is an intelligent agent designed to provide personalized diet and nutrition recommendations based on user input. It leverages advanced language models and can be integrated into multi-agent health care systems to help users make informed dietary choices.

## Features
- Analyzes user input to suggest balanced diet plans.
- Utilizes state-of-the-art language models for natural language understanding.
- Can be extended to integrate with external data sources or APIs for up-to-date nutrition information.
- Designed to assist users in achieving their health and wellness goals.

## Usage
This agent is intended to be used as part of a multi-agent health care system. It can answer questions such as:
- "What is a good diet plan for weight loss?"
- "Suggest a vegetarian meal plan for a week."
- "How much protein should I consume daily?"

## How It Works
- The agent receives user queries related to diet and nutrition.
- It analyzes the input and provides tailored recommendations or meal plans.
- Optionally, it can fetch additional information from external sources if configured.

## Configuration
- **Name:** diet_planner_agent
- **Description:** Agent to provide personalized diet and nutrition recommendations
- **Instruction:** You are a helpful agent who can suggest diet plans and nutrition advice by analyzing the user's input.
- **Tools:** (Add any integrated tools or APIs here, if applicable)

## Requirements
- Python 3.8+
- Dependencies as specified in the parent project's `requirements.txt`
- (Optional) Access to external nutrition APIs if integrated

## File Structure
- `agent.py`: Main agent definition and configuration.
- `agent_executor.py`: (If present) Handles agent execution logic.
- `__main__.py`: Entry point for running the agent as a standalone module.

## How to Run

You can run the Diet Planner Agent as a standalone module using the following command from the `diet_planner_agent` directory:

```
python -m diet_planner_agent
```

Make sure all dependencies are installed and you are in the correct environment. For example:

1. Install dependencies (from the project root):
   ```
   pip install -r requirements.txt
   ```
2. Navigate to the `diet_planner_agent` directory:
   ```
   cd health_care_multiagent/diet_planner_agent
   ```
3. Run the agent:
   ```
   python -m diet_planner_agent
   ```

The agent will start and be ready to receive queries about diet and nutrition.

## Example
```
User: Suggest a high-protein vegetarian meal plan.
Diet Planner Agent: Here is a sample high-protein vegetarian meal plan for a day: Breakfast: Greek yogurt with nuts, Lunch: Lentil salad, Dinner: Tofu stir-fry with vegetables, Snacks: Roasted chickpeas.
```


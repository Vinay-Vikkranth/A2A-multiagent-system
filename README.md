# Health Care Multi-Agent System (A2A, LangGraph & ADK Integration)

## 🚀 Introduction
This project is the best-in-class demonstration of a true multi-agent orchestration platform, seamlessly integrating both LangGraph agents and Google ADK (Agent Development Kit) agents under a unified Host Agent. It showcases the power of Agent-to-Agent (A2A) communication, enabling advanced, modular, and scalable health care solutions.

## 🌟 What Makes This Project Unique?
- **Dual Integration:** Combines the strengths of LangGraph agents (for flexible, graph-based reasoning and workflows) and ADK agents (for robust, production-grade orchestration and Google ecosystem integration).
- **Unified Host Agent:** The Host Agent intelligently routes user queries to the most suitable agent—whether it's a LangGraph or ADK agent—ensuring optimal results for every request.
- **True A2A Protocol:** Implements Google's A2A protocol for secure, scalable, and interoperable agent communication.
- **Plug-and-Play Agents:** Easily add, remove, or upgrade agents (diet, sleep, weather, etc.) without changing the core system.
- **Gradio UI:** Provides an interactive, user-friendly web interface for seamless user interaction with the multi-agent system.
- **SQL Database Integration:** All relevant data and user interactions are stored permanently using an SQL database, ensuring persistence and reliability.

## 🧠 How It Works
1. **User Query:** The user submits a health-related query (e.g., diet plan, sleep advice, weather info for travel) via the Gradio UI.
2. **Host Agent Decision:** The Host Agent analyzes the query and determines which agent (LangGraph or ADK) is best suited to handle it.
3. **Agent Execution:**
   - If the query requires advanced reasoning or workflow, it is routed to a LangGraph agent.
   - If the query benefits from Google ADK's orchestration or needs to interact with external MCP servers, it is routed to an ADK agent.
4. **Response Aggregation:** The Host Agent collects the response and returns a unified answer to the user, while all relevant data is stored in the SQL database for future reference.

## 🏗️ Key Features
- **A2A Protocol:** Secure, scalable agent-to-agent communication.
- **LangGraph Integration:** Enables graph-based, multi-step reasoning and flexible workflows.
- **ADK Integration:** Leverages Google's ADK for robust orchestration and access to the Google ecosystem.
- **Extensible Agent Registry:** Add new agents (e.g., exercise, mental health) with minimal configuration.
- **Modern Python Tooling:** Uses `uv` for dependency management and Python 3.13+ for async performance.
- **Gradio UI:** Modern, interactive web interface for user queries and results.
- **SQL Database:** Persistent storage of user data, queries, and agent responses.
- **Secure Configuration:** All secrets and API keys managed via `.env` files.

## 🛠️ How to Run
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Set up environment variables:**
   - Create `.env` files for each agent as needed (see examples below).
3. **Start sub agents:**
   - Navigate to each sub-agent directory (e.g., `sleep_agent`, `diet_planner_agent`) and start them individually:
     ```bash
     cd health_care_multiagent/sleep_agent
     uv run .
     ```
     ```bash
     cd health_care_multiagent/diet_planner_agent
     uv run .
     ```
   - Repeat for any additional sub-agents you add to the system.
4. **Start the Host Agent:**
   ```bash
   cd health_care_multiagent/host_agent
   uv run .
   ```

## 🗂️ Example .env for Host Agent
```bash
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="your_project"
GOOGLE_CLOUD_LOCATION=us-central1
AIR_AGENT_URL=http://localhost:10002
WEA_AGENT_URL=http://localhost:10001
```

## 🖼️ Architecture
![architecture](assets/A2A_multi_agent.png)

## 💡 Example Queries
- "Suggest a healthy vegetarian meal plan for next week."
- "How many hours should a 25-year-old sleep?"

### 🖥️ Example Screenshots

#### HOW TO RUN
![HOW_TO_RUN]health_care_multiagent\assets\Screenshot 2025-07-10 104110.png()

#### Gradio GUI
![Gradio_GUI](health_care_multiagent\assets\Screenshot 2025-07-10 104201.png)

#### Host-Agent to Sub-Agent
![hostAgent_to_subAgent](health_care_multiagent\assets\Screenshot 2025-07-10 104220.png)

#### Sub-Agent to Host-Agent
![subAgent_to_hostAgent](health_care_multiagent\assets\Screenshot 2025-07-10 104242.png)

#### Final Answer
![Final_Answer](health_care_multiagent\assets\Screenshot 2025-07-10 104306.png)


## 📚 References
- [Google A2A Python SDK](https://github.com/google/a2a-python)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Google ADK Docs](https://google.github.io/adk-docs/)

## ⚠️ Disclaimer
This project is for demonstration and research purposes. Always validate and sanitize agent responses before using them in production.
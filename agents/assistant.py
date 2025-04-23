from langchain_ollama import Ollama
from langchain.agents import initialize_agent, AgentType
from .tools import *

def get_agent():
    model = Ollama(model="mistral", temperature=0.1, max_tokens=512)
    tools = [add_todo_tool, show_todo_tool,delete_todo_tool, add_reminder_tool,show_reminders_tool, delete_reminder_tool]
    agent = initialize_agent(
        tools=tools,
        llm=model,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    return agent
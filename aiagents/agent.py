from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import http_request

model = OllamaModel(
    host="http://localhost:11434",
    model="qwen2.5:1.5b",
    temperature=0.7,
)

system_prompt = """
You are an AI agent.
You may use tools when needed.
You are allowed to make HTTP API calls to public APIs that do not require API keys.
"""

agent = Agent(
    model=model,
    system_prompt=system_prompt,
    tools=[http_request],
)

user_input = input("YOU: ")
response = agent(user_input)
print("AGENT:", response)

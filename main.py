from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.globals import set_debug
from tools import TOOLS
load_dotenv()
set_debug(True) 



class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


llm = ChatOpenAI(model="gpt-5.2")

tools = TOOLS



agent = create_agent(
    model=llm,
    tools=tools,
    response_format=ResearchResponse, 
    system_prompt=(
        "You are a research assistant that generates structured research.\n"
        "Use tools when necessary.\n"
        "Return structured output only."
    ),
)

query = input("What can I help you research? ")

response = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": query}
        ]
    }
)
structured_response: ResearchResponse = response["structured_response"]
print("\n--- Structured Response ---\n")
print(structured_response)
print("\nSummary:\n", structured_response.summary)
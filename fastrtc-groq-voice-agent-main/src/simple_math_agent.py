from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from loguru import logger
from langchain_core.tools import tool

from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    max_tokens=512,
)

@tool
def sum_numbers(a: str, b: str) -> str:
    """Sum two numbers together."""
    a_float, b_float = float(a), float(b)
    result = a_float + b_float
    logger.info(f"➕ Calculating sum: {a} + {b} = {result}")
    return str(result)

@tool
def multiply_numbers(a: str, b: str) -> str:
    """Multiply two numbers together."""
    a_float, b_float = float(a), float(b)
    result = a_float * b_float
    logger.info(f"✖️ Calculating product: {a} × {b} = {result}")
    return str(result)


tools = [sum_numbers, multiply_numbers]

memory = InMemorySaver()

agent = create_agent(
    model=model,
    tools=tools,
    checkpointer=memory,
    )

agent_config = {"configurable": {"thread_id": "default_user"}}

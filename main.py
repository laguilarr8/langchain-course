import os
import certifi
from dotenv import load_dotenv

# 1. Configurar los certificados
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

# 2. Forzar la lectura del archivo .env actual
load_dotenv(override=True)

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from langsmith import wrappers

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return "Tokyo weather is sunny"

# Usamos el modelo estándar
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
tool = [search]
agent = create_agent(model=llm, tools=tool)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="What is the weather in Tokyo?")]})
    print(result)
    

if __name__ == "__main__":
    main()
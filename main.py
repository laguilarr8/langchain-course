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
from langchain_tavily import TavilySearch  # Herramienta de busqueda de Tavily

from langsmith import wrappers






# Usamos el modelo estándar
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")   # gemini-2.5-pro  # gemini-2.5-flash
tool = [TavilySearch()]
agent = create_agent(model=llm, tools=tool)


def main():

    result = agent.invoke({"messages": [HumanMessage(content="Search for 2 job postings for an ai engineer using langchain on linkedingt and list their details")]})
    print(result)
    

if __name__ == "__main__":
    main()
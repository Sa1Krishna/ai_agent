from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Search for the query on the internet and return the results.
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)

llm = ChatOpenAI()
tools = [search]
agent = create_agent(model=llm,tools=tools)

def main():
    print("Hello from tavily!")
    results = agent.invoke({"messages": [HumanMessage(content="Search for top 3 job positings for an ai engineer in langchain in bangalore in linkedin and list all of their details?")]})
    print(results)

if __name__ == "__main__":
    main()
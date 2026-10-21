import os

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()


def search_web(query):
    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        raise ValueError("TAVILY_API_KEY is missing. Add it to your .env file.")

    client = TavilyClient(api_key=api_key)
    response = client.search(query=query, max_results=5)
    return response["results"]
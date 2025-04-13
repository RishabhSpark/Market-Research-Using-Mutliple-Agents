import os
from typing import Any
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

def search_with_tavily(query: str) -> str:
    tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    results: dict[str, Any] = tavily.search(query=query, search_depth='advanced', include_answer=True, max_results=5)
    sources = "\n".join([f"-{result['title']} ({result['url']})" for result in results["results"]])
    return f"{results.get('answer', ' ')}\n\nSources:\n{sources}"
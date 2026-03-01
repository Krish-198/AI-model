from datetime import datetime
from langchain.tools import tool
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper


@tool
def save_text_to_file(data: str) -> str:
    """Save research output into a text file."""
    filename = "research_output.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted = f"\n--- Research Output ---\n{timestamp}\n\n{data}\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted)

    return f"Saved to {filename}"


search_tool = DuckDuckGoSearchRun()

wiki_tool = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(
        top_k_results=1,
        doc_content_chars_max=500,
    )
)

TOOLS = [
    save_text_to_file,
    search_tool,
    wiki_tool,
]
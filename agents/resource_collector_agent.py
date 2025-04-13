import re
from utils.llm import get_gemini_model
from typing import List, Tuple

def search_kaggle(query):
    return  f"https://www.kaggle.com/search?q={query.replace(' ', '+')}"

def search_huggingface(query):
    return f"https://huggingface.co/datasets?search={query.replace(' ', '+')}"


def extract_usecase_titles(usecase_summary: str) -> List[str]:
    pattern = r"Use Case \d+: Title:\s*(.+)"
    return re.findall(pattern, usecase_summary)

def generate_dataset_queries(titles: str) -> List[str]:
    model = get_gemini_model()
    prompt = f"""
    You are a Data Scientist, helping a researcher find public datasets for some use cases. 
    
    For the use cases {titles}, generate 2 short, effective and highly specific search queries that could be used to find datasets on platforms like Kaggle or HuggingFace.
    
    Be concise. Return only the 2 queries as a list, one per line. Do not use quotes or any other formatting.
    Each query should be a single line, and should not include any explanations or additional text. Try to keep it minimal (3-5 words).
    Example output:
    - query 1 (e.g. "Predictive Maintenance Data")
    - query 2 (e.g. "Customer Support Ticket Data")
    """
    output = model.generate_content(prompt).text
    return [line.strip("- ").strip() for line in output.strip().split("\n") if line.strip()]

def collect_dataset_links(usecase_summary: str) -> str:
    titles = extract_usecase_titles(usecase_summary)
    output = ''

    for idx, title in enumerate(titles, 1):
        output += f"#### Use Case {idx}: {title}\n"
        queries = generate_dataset_queries(title)

        for query in queries:
            output += f"- **Query:** `{query}`\n"
            output += f"  - [Kaggle]({search_kaggle(query)})\n"
            output += f"  - [HuggingFace]({search_huggingface(query)})\n"

        output += "\n"

    return output
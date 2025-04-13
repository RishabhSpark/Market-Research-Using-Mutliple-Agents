import re
from utils.llm import get_gemini_model
from typing import List, Tuple

def search_kaggle(query):
    return  f"https://www.kaggle.com/search?q={query.replace(' ', '+')}"

def search_huggingface(query):
    return f"https://huggingface.co/datasets?search={query.replace(' ', '+')}"


def extract_usecase_titles(usecase_summary: str) -> List[str]:
    """
    Extracts use case titles from structured text.
    Example match: "Use Case 1: Title: Predictive Maintenance"
    """
    pattern = r"Use Case \d+: Title:\s*(.+)"
    return re.findall(pattern, usecase_summary)

def generate_dataset_queries(title: str) -> List[str]:
    """
    Use LLM to generate 2 search queries for dataset discovery based on a use case title.
    """
    model = get_gemini_model()
    prompt = f"""
    You are a Data Scientist, helping a researcher find public datasets for some use cases.
    For the use case titled "{title}", generate 2 effective and specific search queries
    that could be used to find datasets on platforms like Kaggle or HuggingFace.
    
    Be concise. Return only the 2 queries as a list, one per line.
    Output should look like:
    - query 1
    - query 2
    """
    output = model.generate_content(prompt).text
    return [line.strip("- ").strip() for line in output.strip().split("\n") if line.strip()]

def collect_dataset_links(usecase_summary: str) -> str:
    """
    Main function to:
    1. Extract use case titles.
    2. Generate search queries for each title.
    3. Return formatted Kaggle and HuggingFace search links.

    Output is in markdown format for Streamlit display.
    """
    titles = extract_usecase_titles(usecase_summary)
    output = "### Dataset Search Links (Kaggle & HuggingFace)\n\n"

    for idx, title in enumerate(titles, 1):
        output += f"#### Use Case {idx}: {title}\n"
        queries = generate_dataset_queries(title)

        for query in queries:
            output += f"- 🔍 **Query:** `{query}`\n"
            output += f"  - [Kaggle]({search_kaggle(query)})\n"
            output += f"  - [HuggingFace]({search_huggingface(query)})\n"

        output += "\n"

    return output

# def run_resource_collector(usecase_summary):
#     lines = usecase_summary.split("\n")
#     keywords = [line.strip() for line in lines if line and not line.startswith("-")][:5]
#     output = "### Datasets:\n"
#     for kw in keywords:
#         output += f"- {kw}\n  - [Kaggle]({search_kaggle(kw)})\n  - [HuggingFace]({search_huggingface(kw)})\n"
#     return output

# def resource_collector(usecase_titles: str, company: str) -> Tuple[str, List[str]]:
#     model = get_gemini_model()

#     prompt = f"""
#     You are a data research assistant helping AI/ML teams. Your task is to identify relevant datasets for each of the following use cases for "{company}". Search and suggest datasets from platforms like Kaggle, HuggingFace, and GitHub.

#     For each use case:
#     - Suggest 1-2 relevant datasets.
#     - Provide a brief explanation for why the dataset is suitable.
#     - Include the direct link to the dataset.

#     Ensure that all suggested datasets are public and well-maintained.

#     Here are all the use cases:
#     {usecase_titles}

#     Return the results in the following format:
#     - Use Case 1: [Title of Use Case 1]
#         - Dataset 1: [Title of Dataset 1]
#             - Description: [Brief description of why this dataset is suitable]
#             - Link: [Direct link to the dataset]
#         - Dataset 2: [Title of Dataset 2]
#             - Description: [Brief description of why this dataset is suitable]
#             - Link: [Direct link to the dataset]
#     """

#     return model.generate_content(prompt).text
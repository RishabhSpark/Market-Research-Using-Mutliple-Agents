from agents.industry_research_agent import industry_research
from agents.usecase_generation_agent import usecase_generation
from agents.resource_collector_agent import collect_dataset_links
from agents.genai_solutions_agent import genai_solutions

def agents_pipeline(industry: str) -> dict:
    """
    Runs the full AI use case pipeline given an industry or company name.

    This function coordinates various sub-components of the pipeline that research the industry, generate AI/ML use cases, 
    suggest relevant datasets, and identify suitable Generative AI tools. The pipeline will return a comprehensive dictionary 
    containing the following outputs:
    
    - Research summary: A concise summary of the industry or company's focus and strategic direction.
    - AI/ML Use Cases: A list of AI/ML use cases proposed for the given industry/company.
    - Dataset Links: Links to relevant datasets on Kaggle and HuggingFace.
    - GenAI Tools: A list of suggested GenAI tools for application within the industry.

    Args:
        industry (str): The name of the industry or company (e.g., "Healthcare", "Retail", "Infosys") for which the AI use case pipeline will be executed.

    Returns:
        dict: A dictionary containing the following keys:
            - "summary": A string with the industry/company research summary.
            - "usecases": A string with AI/ML use cases relevant to the industry/company.
            - "datasets": A string with links to relevant datasets from Kaggle and HuggingFace.
            - "genai_tools": A string with suggested GenAI tools for the industry/company.
    """
    research_summary = industry_research(industry)
    usecases = usecase_generation(research_summary)
    dataset_links = collect_dataset_links(usecases)
    genai_tools = genai_solutions(usecases)

    return {
        "summary": research_summary,
        "usecases": usecases,
        "datasets": dataset_links,
        "genai_tools": genai_tools,
    }
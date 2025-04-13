from agents.industry_research_agent import industry_research
from agents.usecase_generation_agent import usecase_generation
from agents.resource_collector_agent import collect_dataset_links
from agents.genai_solutions_agent import genai_solutions

def agents_pipeline(industry: str) -> dict:
    """
    Runs the full AI use case pipeline given an industry or company name.
    Returns a dictionary with all the outputs.
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
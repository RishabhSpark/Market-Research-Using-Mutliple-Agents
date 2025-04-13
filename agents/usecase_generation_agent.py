from typing import List
from utils.llm import get_gemini_model

def usecase_generation(company_or_industry_summary: str) -> str:
    model = get_gemini_model()

    prompt = f"""
    You are an expert in Artificial Intelligence and Machine Learning applications across industries. Based on the provided company or industry summary, your task is to:

    1. Analyze the current industry trends and standards within the sector, specifically focusing on the use of AI, ML, and automation.
    2. Propose up to 3 actionable and relevant use cases where the company or industry can effectively adopt Generative AI, LLMs, or Machine Learning.

    Each use case should:
    - Be practical and aligned with the strategic and operational needs of the company/industry.
    - Clearly describe how the AI/ML solution can be implemented.
    - Explain the potential business impact — such as increased efficiency, improved decision-making, enhanced customer experience, or cost savings.

    Your response should be:
    - Specific, insightful, and grounded in the context of the industry summary.
    - Professional in tone, with no unnecessary introductions or conclusions.

    Structure your response as follows:
    - Use Case 1: Title: [Title of Use Case 1]
        - Description: [Brief description of Use Case 1]
        - Business Impact: [Expected business impact of Use Case 1]
        - Implementation: [How to implement Use Case 1]

    Here's the summary for the industry/company:
    {company_or_industry_summary}
    """

    # # Generate content using the model
    # response = model.generate_content(prompt)
    return model.generate_content(prompt).text
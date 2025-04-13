from typing import Any
from utils.llm import get_gemini_model
from utils.search import search_with_tavily


def industry_research(company_or_industry):
    model = get_gemini_model()
    research = search_with_tavily(f"{company_or_industry} AI ML Trends and Business overview")
    prompt = f"""
        You are an expert market researcher and analyst. Your task is to analyze a given company and provide concise, structured insights based on publicly available knowledge.

        For the company (or industry) {company_or_industry}, please return the following:

        - Industry Sector - The broader industry or market segment the company operates in (e.g., Automotive, Manufacturing, Finance, Retail, Healthcare).
        - Main Products/Services - A short list of the company's key offerings (products or services).
        - Strategic Focus Areas - What the company is focusing on strategically (e.g., operations, supply chain, customer experience, AI, innovation, sustainability).
        - (Optional) AI/Digital Transformation Trends - If relevant, mention any use of AI, cloud, or digital innovation that aligns with the company's strategic vision.
        
        Keep your response brief, professional, and factual. Avoid including opinions, recommendations, key takeaways, or summaries.

        Structure your response as:
        - Industry Sector: [Industry Sector]
        - Main Products/Services: [Main Products/Services]
        - Strategic Focus Areas: [Strategic Focus Areas]
        - AI/Digital Transformation Trends: [AI/Digital Transformation Trends]
    """

    response = model.generate_content(prompt)
    return response.text
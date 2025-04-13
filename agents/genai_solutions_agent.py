from utils.llm import get_gemini_model

def genai_solutions(summary: str) -> str:
    model = get_gemini_model()
    prompt = f"""
    You are a Generative AI consultant with deep expertise in enterprise AI adoption.
    Based on the following company or industry summary, propose 3 specific GenAI solutions that can be practically applied to enhance productivity, operations, and customer interactions.

    Focus your suggestions on areas like:
    - Document and knowledge search (internal or customer-facing)
    - Automated report or insight generation
    - AI-powered virtual assistants or chatbots
    - Intelligent data extraction and summarization
    - Personalized customer engagement
    - Workflow automation using LLMs

     Structure your response as follows:
     - GenAI Solution 1: Title: [Title of Solution 1]
        - Overview: [Brief overview of Solution 1]
        - Primary Beneficiaries: [Key benefits of Solution 1]
        - Key Advantages: [Advantages of Solution 1]
        - Business Impact: [Expected business impact of Solution 1]
        - Risks or Considerations: [Any risks or considerations for Solution 1]
        - Implementation/Approach: [How to implement Solution 1]


    For each of these, here's what I need.
    - Title: A catchy title for the solution.
    - Overview: A short explanation of what the solution does and its core purpose. Write this like a pitch: what problem it solves and how.
    - Primary Beneficiaries: Who will benefit from this solution? Be specific about the departments or roles (e.g., internal teams, customers, management, support agents, etc.)
    - Key Advantages: List 2-3 tangible benefits. These should relate to either efficiency, cost, accuracy, experience, or innovation. Format as a short bullet list or inline.
    - Business Impact: Explain how the solution directly affects business operations or strategy. Can include measurable or qualitative imporovements.
    - Risks or Considerations: Any known limitations or things to keep in mind.
    - Implementation Approach: Brief technical outline of how this can be implemented. Mention the tools/tech (e.g., RAG with Gemini, LangChain, FastAPI, private embeddings, etc.). Keep it simple but insightful.

    Keep your tone clear, professional, and actionable.

    {summary}
    """

    return model.generate_content(prompt).text
from utils.llm import get_gemini_model

def run_genai_solutions(industry_summary):
    model = get_gemini_model()
    prompt = f"""
    Based on this industry data, suggest GenAI tools such as :
- Document Search (e.g., internal knowledge base)
- Report Generator
- Chatbot

Format in markdown:
### Tool Name
- Description
- Who Benefits 
- advantages of using this Tool
- how it improves productivity,business outcomes, and/or employee experience
- example use cases

{industry_summary}
"""
    return model.generate_content(prompt).text
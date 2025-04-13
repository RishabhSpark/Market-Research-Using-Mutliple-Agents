import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_model() -> genai.GenerativeModel:
    """
    Initializes and returns an instance of the Gemini Generative AI model.

    Returns:
        genai.GenerativeModel: An instance of the Gemini Generative AI model, ready to be used for generating content and AI tasks.
    """
    return genai.GenerativeModel("gemini-1.5-flash-8b")
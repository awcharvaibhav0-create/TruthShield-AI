import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")

def fact_check(claim):

    prompt = f"""
    Fact-check this claim:

    {claim}

    Return:
    - Verdict
    - Explanation
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except ResourceExhausted:
        return "⚠️ Gemini quota exceeded. Please try again later."

    except Exception as e:
        return f"Error: {str(e)}"
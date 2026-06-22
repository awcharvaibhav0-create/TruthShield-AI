import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

model = genai.GenerativeModel("gemini-flash-latest")

def extract_claim(text):

    prompt = f"""
    Extract the main factual claim from this text.

    Text:
    {text}

    Return only the claim.
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()

    except ResourceExhausted:
        print("Gemini quota exceeded.")
        return text

    except Exception as e:
        print(f"Error: {e}")
        return text
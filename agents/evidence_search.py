from google import genai
import json

client = genai.Client()

def search_evidence(claim):

    prompt = f"""
    Analyze this claim:

    {claim}

    Return JSON only in this format:

    {{
        "supporting": [
            "evidence 1",
            "evidence 2"
        ],
        "contradicting": [
            "evidence 1",
            "evidence 2"
        ]
    }}

    Do not return markdown.
    """

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return json.loads(response.text)

    except Exception as e:
        return {
    "supporting": [
        {
            "title": "WHO",
            "url": "https://www.who.int"
        }
    ],
    "contradicting": [
        {
            "title": "Reuters Fact Check",
            "url": "https://www.reuters.com/fact-check"
        }
    ]
}
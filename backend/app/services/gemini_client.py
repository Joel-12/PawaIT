import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

async def get_llm_response(question: str) -> str:
    try:
        # Load the Gemini Pro model
        model = genai.GenerativeModel(model_name="gemini-1.5-pro")

        # Prompt engineering: formatted instructions for consistent output
        prompt = f"""
You are a helpful travel assistant AI.

Please provide a well-structured and informative answer to the following travel question:
"{question}"

Your response should be formatted into the following sections:
1. Visa Requirements
2. Passport Validity
3. Health/Vaccination Requirements
4. Travel Advisories
5. Other Travel Tips (if relevant)

Keep your tone professional and clear.
"""

        # Call Gemini with the prompt
        response = model.generate_content(prompt)

        # Return the plain text from the LLM
        return response.text

    except Exception as e:
        return f"An error occurred while generating a response: {str(e)}"

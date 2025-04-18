Documentation of Prompts Used with the LLM:
The AI Travel Assistant uses structured prompts to interact with the Large Language Model (LLM) 
via Google's Gemini API. These prompts are carefully designed to ensure the model generates 
accurate, professional, and structured responses to travel-related queries.

Prompt Structure:
The prompts sent to the LLM follow a structured format to guide the model in generating 
relevant and detailed responses. Below is an example of the prompt structure:

  You are an AI Travel Assistant. Your task is to provide detailed and structured travel advice to users. 
  The response should include the following sections:
    1. Visa Requirements: Provide information about visa requirements for the destination.
    2. Passport Validity: Mention the minimum passport validity required for travel.
    3. Health/Vaccination Requirements: List any health advisories or vaccination requirements.
    4. Travel Advisories: Include any government-issued travel advisories or warnings.
    5. Other Travel Tips: Provide additional tips such as currency, language, or cultural norms.

  User Query: "{user_question}"

  Please provide a detailed and professional response in the format specified above.

Example Prompts:
Here are some example prompts used with the LLM:

Prompt 1: Visa Requirements
    You are an AI Travel Assistant. Provide detailed travel advice for the following query:
    "What are the visa requirements for traveling to Japan?"

      Response Format:
    1. Visa Requirements
    2. Passport Validity
    3. Health/Vaccination Requirements
    4. Travel Advisories
    5. Other Travel Tips

Prompt 2: Health and Safety
    You are an AI Travel Assistant. Provide detailed travel advice for the following query:
    "Are there any health or vaccination requirements for visiting South Africa?"

      Response Format:
    1. Visa Requirements
    2. Passport Validity
    3. Health/Vaccination Requirements
    4. Travel Advisories
    5. Other Travel Tips

Prompt 3: General Travel Tips
    You are an AI Travel Assistant. Provide detailed travel advice for the following query:
    "What are some travel tips for visiting Paris, France?"

      Response Format:
    1. Visa Requirements
    2. Passport Validity
    3. Health/Vaccination Requirements
    4. Travel Advisories
    5. Other Travel Tips

How Prompts Are Used:
User Input: The user enters a travel-related question in the frontend (e.g., "What are the visa 
  requirements for traveling to Japan?").
Prompt Construction: The backend constructs a structured prompt using the user's question and 
  the predefined format.
LLM Interaction: The prompt is sent to the LLM (via the Gemini API), which generates a detailed 
  response.
Response Parsing: The backend parses the response and sends it back to the frontend for display.

Why Use Structured Prompts?:
Consistency: Ensures that all responses follow a predictable and professional format.
Clarity: Makes it easier for users to understand the information provided.
Relevance: Guides the LLM to focus on specific aspects of travel advice.

Customizing Prompts:
You can customize the prompts in the gemini_client.py file to include additional sections or 
modify the tone of the responses. For example, you can add sections like "Local Transportation 
Options" or "Weather Conditions."

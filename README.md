# AI Travel Assistant 🌍

The AI Travel Assistant is a web application that leverages advanced AI models to provide users with detailed and structured answers to travel-related questions. It integrates with Google's Gemini API to generate responses and uses FastAPI for the backend and Streamlit for the frontend.

---

## Features
- **AI-Powered Responses**: Uses Google's Gemini API to generate structured and professional travel advice.
- **FastAPI Backend**: A lightweight and efficient backend for handling API requests.
- **Streamlit Frontend**: A user-friendly interface for interacting with the assistant.
- **Structured Travel Information**: Responses include sections like visa requirements, health advisories, and travel tips.

---

## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- Node.js (optional, for frontend extensions)
- A valid API key for Google's Gemini API, enable gemini API on this https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com
    then generate key here https://makersuite.google.com/app/apikey

### Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/ai-travel-assistant.git
   cd ai-travel-assistant/
   ```
### Environment 
    After cd into ai-travel-assistant, create a virtual environment 
    using this command : sudo apt install python3-venv
                         python3 -m venv venv
                         source venv/bin/activate
    After that cd into backend folder, then run this command : cp .env.example .env
    then input your gemini api key on the .env file.
    Then run this command : pip install -r requirements.txt.
    once finished again run this command : uvicorn app.main:app --host 0.0.0.0 --port 9000 --reload,
        this will start the fastapi service at http://localhost:9000/docs.
    
    open another terminal and cd ai-travel-assistant/frontend and run : stream,lit run app.py,
        this will also open the ui at http://localhost:8501. In this ui you will interact with
        the model by asking travel questions.

DONE!!!

Open the frontend in your browser (http://localhost:8501).
Enter a travel-related question in the input field (e.g., "What are the visa requirements for traveling to Japan?").
Click the Submit button.
The AI Travel Assistant will process your query and return a structured response with sections like:
Visa Requirements
Passport Validity
Health/Vaccination Requirements
Travel Advisories
Other Travel Tips
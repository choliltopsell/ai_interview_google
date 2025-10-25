# services/gemini_service.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash-live")

def ask_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error dari Gemini: {str(e)}"


def generate_interview_answer(question: str, profile: dict):
    prompt = f"""
    You are an AI English interview coach helping this candidate prepare for job interviews.

    Candidate Profile:
    {profile}

    Instructions:
    1. Answer the question professionally in English.
    2. Then provide the translation in Indonesian below.
    3. Use relevant experience, skills, and achievements.
    4. If there are multiple experiences, choose the most relevant one.
    5. Keep the tone confident and natural.

    Question: "{question}"
    """

    return ask_gemini(prompt)

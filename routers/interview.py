# routers/interview.py

from fastapi import APIRouter
from pydantic import BaseModel
from services.gemini_service import generate_interview_answer
from services.memory_service import get_profile

router = APIRouter()

class InterviewQuestion(BaseModel):
    question: str


@router.post("/interview")
def interview_ai(data: InterviewQuestion):
    profile = get_profile()

    if not profile:
        return {"message": "❌ Profil belum diatur. Tambahkan profil dulu lewat /ai/profile."}

    ai_response = generate_interview_answer(data.question, profile)
    return {"result": ai_response}

# routers/profile.py

from fastapi import APIRouter
from pydantic import BaseModel
from services.memory_service import set_profile, get_profile

router = APIRouter()

class Experience(BaseModel):
    company: str
    position: str
    duration: str
    responsibilities: list[str]
    achievements: list[str]

class Profile(BaseModel):
    name: str
    target_position: str
    skills: list[str]
    summary: str
    experiences: list[Experience]
    additional_description: str


@router.post("/profile")
def save_profile(profile: Profile):
    set_profile(profile.dict())
    return {"message": "✅ Profil kandidat berhasil disimpan!", "data": profile}


@router.get("/profile")
def view_profile():
    profile = get_profile()
    if not profile:
        return {"message": "❌ Profil belum diatur. Gunakan POST /ai/profile untuk menambahkan."}
    return {"profile": profile}

from fastapi import FastAPI
from routers import profile, interview

app = FastAPI(
    title="AI Interview Assistant (Gemini)",
    description="Asisten AI untuk latihan interview berbahasa Inggris & Indonesia dengan profil pengguna yang dapat disesuaikan.",
    version="1.0.0"
)

# Router
app.include_router(profile.router, prefix="/ai", tags=["Profile"])
app.include_router(interview.router, prefix="/ai", tags=["Interview Assistant"])

@app.get("/")
def root():
    return {
        "message": "🚀 AI Interview Assistant aktif!",
        "endpoints": {
            "/ai/profile": "Atur atau lihat profil kandidat",
            "/ai/interview": "Latihan interview (POST)"
        }
    }

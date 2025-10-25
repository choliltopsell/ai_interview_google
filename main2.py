from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import profile, interview

app = FastAPI(
    title="AI Interview Assistant (Gemini)",
    description="Asisten AI untuk latihan interview berbahasa Inggris & Indonesia dengan profil pengguna yang dapat disesuaikan.",
    version="1.0.0"
)

# --- Middleware CORS ---
# Ini penting biar bisa diakses dari frontend (misalnya Next.js, React, dsb)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # kalau mau aman bisa diganti ke domain Next.js kamu misalnya ["https://my-frontend.vercel.app"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Router Registration ---
app.include_router(profile.router, prefix="/ai", tags=["Profile"])
app.include_router(interview.router, prefix="/ai", tags=["Interview Assistant"])


# --- Root endpoint ---
@app.get("/")
def root():
    return {
        "message": "🚀 AI Interview Assistant aktif!",
        "docs": "/docs",
        "endpoints": {
            "/ai/profile": "Atur atau lihat profil kandidat",
            "/ai/interview": "Latihan interview (POST)"
        }
    }

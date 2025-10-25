# services/memory_service.py

from typing import Optional

# Simpan data profil secara sederhana (bisa diganti ke database)
user_profile: Optional[dict] = None

def set_profile(profile_data: dict):
    global user_profile
    user_profile = profile_data

def get_profile() -> Optional[dict]:
    return user_profile

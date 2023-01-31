import hashlib

from app.config import PASSWORD_SECRET


def get_password_hash(password: str) -> str:
    return hashlib.sha256(f"{PASSWORD_SECRET}{password}".encode("utf-8")).hexdigest()

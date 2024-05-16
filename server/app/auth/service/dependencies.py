from app.config import (
    JWT_SECRET,
    JWT_ALGORITHM,
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES
)

from .service import AuthService


def get_auth_service():
    return AuthService(
        secret_key=JWT_SECRET,
        algorithm=JWT_ALGORITHM,
        access_token_expire_minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

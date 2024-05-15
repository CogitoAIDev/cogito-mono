from datetime import timedelta

from jose import jwt

from .interface import IAuthService


class AuthService(IAuthService):
    def __init__(
        self,
        secret_key: str,
        algorithm: str,
        access_token_expire_minutes: int
    ): ...

    async def create_access_token(
        self,
        data: dict[str, any],
        expires_delta: timedelta | None = None
    ): ...

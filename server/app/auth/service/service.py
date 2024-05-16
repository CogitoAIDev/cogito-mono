from datetime import datetime, timedelta
from jose import jwt, JWTError

from .interface import IAuthService


class AuthService(IAuthService):
    def __init__(
        self,
        secret_key: str,
        algorithm: str,
        access_token_expire_minutes: int
    ):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.access_token_expire_minutes = access_token_expire_minutes

    def create_access_token(
        self,
        data: dict[str, any]
    ):
        to_encode = data.copy()
        expire = datetime.now(datetime.UTC) + \
            timedelta(minutes=self.access_token_expire_minutes)

        to_encode["exp"] = expire
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)

    def verify_token(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, self.secret_key,
                                 algorithms=[self.algorithm])
            username: str = payload.get("username")
            if username is None:
                raise ValueError("Invalid token")
            return payload
        except JWTError as e:
            raise ValueError("Invalid token") from e

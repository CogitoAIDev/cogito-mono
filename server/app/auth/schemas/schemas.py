from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData:
    user_id: int
    username: str | None


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

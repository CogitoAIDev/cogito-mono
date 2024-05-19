from typing import Optional
from pydantic import (
    BaseModel,
    Json,
    EmailStr,
    model_validator,
    field_validator,
)


class UserBase(BaseModel):
    user_id: Optional[int] = None
    user_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    tg_user_id: Optional[int] = None
    context: Optional[Json] = None


class UserCreateDTO(UserBase):
    ...


class EmailRegisterDTO(UserBase):
    email: EmailStr
    password: str

    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        if ' ' in v or len(v) < 8:
            raise ValueError('Bad Password')
        return v


class TelegramRegisterDTO(UserBase):
    tg_user_id: int


class UserUpdateDTO(UserBase):
    @model_validator(mode='before')
    @classmethod
    def check_user_id(cls, values):
        if 'user_id' in values and values['user_id'] is not None:
            raise ValueError("user_id should not be provided in UserUpdateDTO")
        return values


class UserResponseDTO(UserBase):
    user_id: int

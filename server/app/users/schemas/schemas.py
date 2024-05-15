from pydantic import BaseModel, Json, model_validator, EmailStr


class UserBase(BaseModel):
    user_id: int | None
    user_name: str | None
    email: EmailStr | None
    tg_user_id: int | None
    context: Json | None


class UserCreateDTO(UserBase):
    user_name: str
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

from app.users.schemas import (
    UserResponseDTO,
    UserCreateDTO,
    UserUpdateDTO,
)

from .interface import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self):
        ...

    def get_users_by_ids(
        self, 
        user_ids: list[int]
    ) -> list[UserResponseDTO] | None: ...

    def get_user_by_id(
        self, user_id: int
    ) -> UserResponseDTO | None: ...

    def get_user_by_filters(
        self, filters: dict | None
    ) -> UserResponseDTO | None: ...

    def create_user(
        self, user_data: UserCreateDTO
    ) -> UserResponseDTO | None: ...

    def update_user(
        self, user_data: UserUpdateDTO
    ) -> UserResponseDTO | None: ...

from abc import ABC, abstractmethod

from app.users.schemas import (
    UserCreateDTO,
    UserUpdateDTO,
    UserResponseDTO
)


class IUserService(ABC):
    @abstractmethod
    async def find_users(
        self, user_ids: list[int], filters: dict | None
    ) -> list[UserResponseDTO] | None: ...

    @abstractmethod
    async def find_user_by_id(
        self, user_id: int
    ) -> UserResponseDTO | None: ...

    @abstractmethod
    async def find_user_with_filters(
        self, filters: dict | None
    ) -> UserResponseDTO | None: ...

    @abstractmethod
    async def register_user(
        self, user_data: UserCreateDTO
    ) -> UserResponseDTO | None: ...

    @abstractmethod
    async def update_user(
        self, user_data: UserUpdateDTO
    ) -> UserResponseDTO | None: ...

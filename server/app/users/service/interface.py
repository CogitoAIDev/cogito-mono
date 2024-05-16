from typing import Optional
from abc import ABC, abstractmethod

from app.users.schemas import (
    UserCreateDTO,
    UserUpdateDTO,
    UserResponseDTO
)


class IUserService(ABC):
    @abstractmethod
    async def find_users(
        self,
        user_ids: list[int],
        filters: dict | None
    ) -> Optional[list[UserResponseDTO]]: ...

    @abstractmethod
    async def find_user_by_id(
        self, user_id: int
    ) -> Optional[UserResponseDTO]: ...

    @abstractmethod
    async def find_user_by_filters(
        self, filters: dict | None
    ) -> Optional[UserResponseDTO]: ...

    @abstractmethod
    async def register_user(
        self, user_data: UserCreateDTO
    ) -> Optional[UserResponseDTO]: ...

    @abstractmethod
    async def update_user(
        self, user_data: UserUpdateDTO
    ) -> Optional[UserResponseDTO]: ...

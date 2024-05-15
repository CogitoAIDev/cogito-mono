from abc import ABC, abstractmethod

from app.users.schemas import UserCreateDTO, UserUpdateDTO, UserResponseDTO


class IUserRepository(ABC):
    @abstractmethod
    def get_users(
        self, user_ids: list[int], filters: dict | None
    ) -> list[UserResponseDTO] | None: ...

    @abstractmethod
    def get_user_by_id(
        self, user_id: int
    ) -> UserResponseDTO | None: ...

    @abstractmethod
    def get_user_with_filters(
        self, filters: dict | None
    ) -> UserResponseDTO | None: ...

    @abstractmethod
    def create_user(
        self, user_data: UserCreateDTO
    ) -> UserResponseDTO | None: ...

    @abstractmethod
    def update_user(
        self, user_data: UserUpdateDTO
    ) -> UserResponseDTO | None: ...

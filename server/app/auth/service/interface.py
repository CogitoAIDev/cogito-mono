from abc import ABC, abstractmethod
from datetime import timedelta


class IAuthService(ABC):

    @abstractmethod
    async def create_access_token(
        self, data: dict[str, any], expires_delta: timedelta | None = None
    ) -> str: ...

    @abstractmethod
    async def verify_token(
        self, token: str
    ) -> dict[str, any]: ...

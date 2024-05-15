from abc import ABC, abstractmethod
from datetime import timedelta


class IAuthService(ABC):

    @abstractmethod
    def create_access_token(
        self, data: dict[str, any], expires_delta: timedelta | None = None
    ) -> str: ...

    @abstractmethod
    def verify_token(
        self, token: str
    ) -> dict[str, any]: ...

from app.users.repository import IUserRepository

from app.auth.service import IAuthService

from .interface import IUserService


class UserService(IUserService):

    def __init__(
        self,
        user_repository: IUserRepository,
        auth_service: IAuthService,
    ) -> None:
        super().__init__()
        self.user_repository = user_repository
        self.auth_service = auth_service


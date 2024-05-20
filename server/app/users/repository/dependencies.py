from app.config import db_pool_connection

from .repository import UserRepository


def get_user_repository():
    return UserRepository(db_connection=db_pool_connection)

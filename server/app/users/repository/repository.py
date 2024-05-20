from psycopg2 import sql
from psycopg2.extras import Json
from psycopg2.errors import UniqueViolation

from app.users.schemas import (
    UserResponseDTO,
    UserCreateDTO,
    UserUpdateDTO,
)
from app.users.exceptions import (
    UserNotFound,
    UniqueDuplicated
)
from app.config import (
    logger,
    DatabaseConnectionPool
)

from .interface import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self, db_connection: DatabaseConnectionPool):
        self.db_connection = db_connection

    def get_users_by_ids(
        self,
        user_ids: list[int]
    ) -> list[UserResponseDTO] | None: ...

    def get_user_by_id(
        self, user_id: int
    ) -> UserResponseDTO | None:
        with self.db_connection.get_connection_with_cursor() as cursor:
            logger.debug(
                f'Inside get_user_by_id user_repository with user_id {user_id}'
            )
            cursor.execute(f'''
SELECT user_id, user_name, email, telegram_user_id, context
FROM users
WHERE user_id = %s;
''', (user_id, ))
            results = cursor.fetchall()
            if not results:
                raise UserNotFound(f'User with {user_id} not found')

            user_tuple = results[0]
            return UserResponseDTO(
                user_id=user_tuple[0],
                user_name=user_tuple[1],
                email=user_tuple[2],
                tg_user_id=user_tuple[3],
                context=user_tuple[4]
            )

    def get_user_by_filters(
        self, filters: dict | None
    ) -> UserResponseDTO: ...

    def create_user(
        self, user_data: UserCreateDTO
    ) -> UserResponseDTO:
        try:
            with self.db_connection.get_connection_with_cursor() as cursor:
                user_fields = user_data.model_dump(exclude_none=True)
                columns = sql.SQL(', ').join(
                    map(sql.Identifier, user_fields.keys())
                )
                values = sql.SQL(', ').join(
                    sql.Literal(Json(v)) if isinstance(
                        v, dict) else sql.Literal(v)
                    for v in user_fields.values()
                )
                logger.debug(values)

                query = sql.SQL('''
INSERT INTO users ({columns})
VALUES ({values})
RETURNING user_id;
''').format(columns=columns, values=values)

                cursor.execute(query)
                new_user_id = cursor.fetchone()[0]
                return UserResponseDTO(user_id=new_user_id)
        except UniqueViolation as e:
            logger.exception(e)
            raise UniqueDuplicated(f'Unique duplicated error: {e}')

    def update_user(
        self, user_data: UserUpdateDTO
    ) -> UserResponseDTO | None: ...

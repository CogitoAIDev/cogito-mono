from psycopg2 import pool
from contextlib import contextmanager

from app.config import logger

from .constants import (
    DB_HOST,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_PORT
)


class DatabaseConnectionPool():
    _connection_pool = None

    def __init__(
        self,
        minconn: int,
        maxconn: int
    ) -> None:
        if self._connection_pool is None:
            try:
                logger.debug(f'DB_HOST: {DB_HOST}, DB_database: {DB_NAME}')
                self._connection_pool = pool.SimpleConnectionPool(
                    minconn,
                    maxconn,
                    database=DB_NAME,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    port=DB_PORT,
                    host=DB_HOST,
                )
                logger.info('Connection pool created')
            except Exception as e:
                logger.error(f"Failed to create connection pool: {e}")
                raise

    @contextmanager
    def get_connection_with_cursor(self):
        conn, cursor = self._get_connection_with_cursor()
        try:
            yield cursor
        except Exception as e:
            conn.rollback()
            raise e
        else:
            conn.commit()
        finally:
            cursor.close()
            self._put_connection(conn)

    def _get_connection_with_cursor(self):
        try:
            conn = self._connection_pool.getconn()
            cursor = conn.cursor()
            return conn, cursor
        except Exception as e:
            logger.error(f"Failed to get connection with cursor: {e}")
            raise

    def _put_connection(self, conn):
        try:
            self._connection_pool.putconn(conn)
        except Exception as e:
            logger.error(f"Failed to put connection back to pool: {e}")
            raise

    def _close_all_connections(self):
        if self._connection_pool:
            try:
                self._connection_pool.closeall()
                logger.info("Connection pool closed")
            except Exception as e:
                logger.error(f"Failed to close all connections: {e}")
                raise


db_pool_connection = DatabaseConnectionPool(1, 10)

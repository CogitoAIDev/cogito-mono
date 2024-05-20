import os
from dotenv import load_dotenv

# Prefix for api URLs
API_PREFIX = '/api/v1'

# Load .env vars from .env file
load_dotenv(
    dotenv_path=os.path.join(
        os.path.dirname(__file__), '../..', '.env'
    )
)


# Logger vars
LEVEL_LOGGING = os.getenv('LEVEL_LOGGING')

# JWT vars
JWT_SECRET = os.getenv('JWT_SECRET')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv('JWT_ACCESS_TOKEN_EXPIRE_MINUTES')
)

# DB vars
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')

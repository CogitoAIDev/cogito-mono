import os
from dotenv import load_dotenv


API_PREFIX = '/api/v1'

load_dotenv(
    dotenv_path=os.path.join(
        os.path.dirname(__file__), '../..', '.env'
    )
)


LEVEL_LOGGING = os.getenv('LEVEL_LOGGING')
JWT_SECRET = os.getenv('JWT_SECRET')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv('JWT_ACCESS_TOKEN_EXPIRE_MINUTES')
)

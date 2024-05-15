from fastapi import FastAPI

from app.config import logger, API_PREFIX
from app.users.api import user_router

app = FastAPI()

app.include_router(user_router, prefix=API_PREFIX)
logger.info('Cogito app is here in mono!')

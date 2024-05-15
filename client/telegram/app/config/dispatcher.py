from aiogram import Dispatcher

from app.handlers import message_router, start_router

dp = Dispatcher()
dp.include_routers(start_router, message_router)

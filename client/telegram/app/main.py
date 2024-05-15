import asyncio
import logging
import sys

from app.config import dp, bot
from app.handlers import start_router, message_router


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

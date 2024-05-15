from aiogram.types import Message
from aiogram import Router, F

message_router = Router()


@message_router.message(F.text)
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender
    """
    await message.send_copy(chat_id=message.chat.id)

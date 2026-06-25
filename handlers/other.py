from aiogram import Router
from aiogram.types import Message


other_router = Router()

@other_router.message()
async def send_answer(message: Message):
    await message.answer(text="Не знаю, как реагировать на такое сообщение")
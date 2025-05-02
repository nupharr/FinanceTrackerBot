from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router1 = Router()


@router1.message(CommandStart())
async def message_start_handler(message: Message):
    await message.answer("Hello!")

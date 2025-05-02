from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router1 = Router()


@router1.message(CommandStart())
async def message_start_handler(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name if message.from_user else "User"}!\nДанный бот предназначен для ослеживания ваших трат.\nЧтобы продолжить, выберите действие."
    )

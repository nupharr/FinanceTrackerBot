from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from src.messages import faq_text
from src.database import add_expense

router1 = Router()


@router1.message(Command("help", "start"))
async def message_help_handler(message: Message):
    await message.answer(faq_text)


@router1.message(F.text)
async def echo(message: Message):
    amount, category = message.text.split() if message.text else ["1", "2"]
    add_expense(
        message.from_user.id if message.from_user else 1, category, float(amount)
    )
    await message.answer(f"Готово!\nВ категорию {category} добавлена сумма {amount}")

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards.reply import menu

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        f"""
👋 Привет {message.from_user.full_name}! Рад помочь тебе с задачами.\n
Я — твой персональный Todo Bot. С этого момента можно выгрузить все дела из головы прямо сюда. Я всё сохраню и вовремя напомню о важном. 🎯\n
⚡️ Быстрый старт — это очень просто:\n
🤖 Чтобы записать задачу: просто отправь мне её текстом в этот чат (например: «Купить кофе завтра в 9:00»).\n
📅 Чтобы настроить напоминание: укажи время прямо в тексте задачи или добавь его позже.\n
Используй меню ниже, чтобы управлять своими делами, или просто напиши своё первое дело прямо сейчас! 👇\n
        """,
        reply_markup=menu
    )



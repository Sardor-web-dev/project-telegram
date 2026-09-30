from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Мои задачи")],
        [KeyboardButton(text="📅 На неделю")],
        [KeyboardButton(text="📂 Списки / Проекты")],
        [KeyboardButton(text="⚙️ Настройки")]

    ],
    resize_keyboard=True,
    one_time_keyboard=False
)



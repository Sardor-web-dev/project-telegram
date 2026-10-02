from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Мои задачи")],
        [KeyboardButton(text="📌 Спрака по боту")],
        [KeyboardButton(text="⚙️ Настройки")]

    ],
    resize_keyboard=True,
    one_time_keyboard=False
)



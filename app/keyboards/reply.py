from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def barbers_keyboard(
        barbers: list[str]
) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    for barber in barbers:
        builder.button(
            text=f"{barber}"
        )

    return builder.as_markup()

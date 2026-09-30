from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def custom_builder() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for i in range(1, 4):
        builder.button(
            text=f"Button {i}",
            callback_data=f"button {i}"

        )

    return builder.as_markup()

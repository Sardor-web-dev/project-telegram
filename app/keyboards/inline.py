from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# menu = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Создать задачу", callback_data="create_task")],
#         [InlineKeyboardButton(text="Мои задачи", callback_data="my_tasks")],
#         [InlineKeyboardButton(text="Моя статистика", callback_data="my_stats")]
#     ],
# )


buttons = [{"text": "📥 Показать задачи", "callback_data": "/list"},{"text": "⚙️ Настроить время","callback_data": "/settings"},{"text": "✍️ Написать в поддержку","callback_data": "https://t.me/Djamolov_Sardor"}]
builder = InlineKeyboardBuilder()
for btn in buttons:
    builder.button(text=btn["text"], callback_data=btn["callback_data"])
builder.adjust(1,2)

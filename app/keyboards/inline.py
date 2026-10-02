from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.utils.user_settings import TIMEZONES

buttons = [{"text": "📥 Показать задачи", "callback_data": "/list"}, {"text": "📝 Поддержка","callback_data": "https://t.me/Djamolov_Sardor"}]
builder = InlineKeyboardBuilder()
for btn in buttons:
    builder.button(text=btn["text"], callback_data=btn["callback_data"])
builder.adjust(2)


def tasks_keyboard(tasks: list[dict]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for task in tasks:
        kb.button(text=f"✅ {task['text']}", callback_data=f"done:{task['id']}")
    kb.adjust(1)
    return kb.as_markup()


def settings_keyboard(current_tz: str, notifications: bool) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for tz in TIMEZONES:
        label = f"✅ {tz}" if tz == current_tz else tz
        kb.button(text=label, callback_data=f"tz:{tz}")
    notif_label = "🔔 Уведомления: Вкл" if notifications else "🔕 Уведомления: Выкл"
    kb.button(text=notif_label, callback_data="toggle_notifications")
    kb.adjust(2, 2, 1)
    return kb.as_markup()

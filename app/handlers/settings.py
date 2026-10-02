from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from app.utils import user_settings
from app.keyboards.inline import settings_keyboard

router = Router()


def settings_text(settings: dict) -> str:
    notif = "включены 🔔" if settings.get("notifications", True) else "выключены 🔕"
    return (
        "⚙️ Настройки\n\n"
        f"Часовой пояс: {settings.get('timezone')}\n"
        f"Уведомления: {notif}\n\n"
        "Выбери часовой пояс или переключи уведомления:"
    )


@router.message(Command("settings"))
@router.message(F.text == "⚙️ Настройки")
async def settings_handler(message: Message):
    settings = user_settings.get_user_settings(message.from_user.id)
    await message.answer(
        settings_text(settings),
        reply_markup=settings_keyboard(settings["timezone"], settings["notifications"]),
    )


@router.callback_query(F.data.startswith("tz:"))
async def set_timezone_callback(callback: CallbackQuery):
    tz = callback.data.split(":", 1)[1]
    user_settings.set_timezone(callback.from_user.id, tz)
    settings = user_settings.get_user_settings(callback.from_user.id)
    await callback.message.edit_text(
        settings_text(settings),
        reply_markup=settings_keyboard(settings["timezone"], settings["notifications"]),
    )
    await callback.answer(f"Часовой пояс установлен: {tz}")


@router.callback_query(F.data == "toggle_notifications")
async def toggle_notifications_callback(callback: CallbackQuery):
    enabled = user_settings.toggle_notifications(callback.from_user.id)
    settings = user_settings.get_user_settings(callback.from_user.id)
    await callback.message.edit_text(
        settings_text(settings),
        reply_markup=settings_keyboard(settings["timezone"], settings["notifications"]),
    )
    await callback.answer("Уведомления включены" if enabled else "Уведомления выключены")
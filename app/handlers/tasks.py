from aiogram.types import CallbackQuery
from aiogram import F, Router

router = Router()

@router.callback_query(F.data == "/list")
async def list_callback_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "Раздел задач: здесь будут ваши задачи"
    )
    await callback.answer()


@router.message(F.text == "📝 Мои задачи")
async def list_handler(message: Message):
    await message.answer(
        "Раздел задач: здесь будут ваши задачи"
    )
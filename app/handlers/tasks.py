from aiogram.types import CallbackQuery, Message
from aiogram import F, Router
from aiogram.filters import Command, CommandObject

from app.utils import db
from app.keyboards.inline import tasks_keyboard

router = Router()


def format_tasks(tasks: list[dict]) -> str:
    if not tasks:
        return "На сегодня активных задач нет. Просто напиши текст, чтобы добавить новую задачу."
    lines = [f"{i}. {t['text']}" for i, t in enumerate(tasks, start=1)]
    return "📋 Твои активные задачи:\n\n" + "\n".join(lines)


@router.callback_query(F.data == "/list")
async def list_callback_handler(callback: CallbackQuery):
    tasks = db.get_tasks(callback.from_user.id)
    await callback.message.edit_text(
        format_tasks(tasks),
        reply_markup=tasks_keyboard(tasks) if tasks else None,
    )
    await callback.answer()


@router.message(F.text == "📝 Мои задачи")
@router.message(Command("list"))
async def list_handler(message: Message):
    tasks = db.get_tasks(message.from_user.id)
    await message.answer(
        format_tasks(tasks),
        reply_markup=tasks_keyboard(tasks) if tasks else None,
    )


@router.callback_query(F.data.startswith("done:"))
async def done_callback_handler(callback: CallbackQuery):
    task_id = int(callback.data.split(":")[1])
    ok = db.make_done(callback.from_user.id, task_id)
    if not ok:
        await callback.answer("Задача не найдена", show_alert=True)
        return

    tasks = db.get_tasks(callback.from_user.id)
    await callback.message.edit_text(
        format_tasks(tasks),
        reply_markup=tasks_keyboard(tasks) if tasks else None,
    )
    await callback.answer("Задача выполнена ✅")


@router.message(Command("done"))
async def done_handler(message: Message, command: CommandObject):
    tasks = db.get_tasks(message.from_user.id)
    if not tasks:
        await message.answer("У тебя нет активных задач.")
        return

    if command.args:
        try:
            index = int(command.args.strip())
            task = tasks[index - 1]
        except (ValueError, IndexError):
            await message.answer("Укажи номер задачи из списка /list, например: /done 1")
            return
        db.make_done(message.from_user.id, task["id"])
        await message.answer(f"✅ Задача «{task['text']}» отмечена выполненной.")
        return

    await message.answer(
        "Выбери задачу для завершения:",
        reply_markup=tasks_keyboard(tasks),
    )


@router.message(F.text & ~F.text.startswith("/"))
async def add_task_handler(message: Message):
    task = db.create_task(message.from_user.id, message.text)
    await message.answer(f"✅ Задача добавлена: «{task['text']}»")
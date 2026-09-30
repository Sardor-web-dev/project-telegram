from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

router = Router()

class RegisterForm(StatesGroup):
    name = State()
    age = State()
    phone = State()

@router.message(Command("register"))
async def register_start(message: Message, state: FSMContext):
    await state.set_state(RegisterForm.name)
    await message.answer("Введите ваше имя:")


@router.message(RegisterForm.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await state.set_state(RegisterForm.age)
    await message.answer("Введите ваш возраст:")


@router.message(RegisterForm.age)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)

    await state.set_state(RegisterForm.phone)
    await message.answer("Введите номер телефона:")


@router.message(RegisterForm.phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)

    data = await state.get_data()

    await message.answer(
        f"Регистрация завершена!\n\n"
        f"Имя: {data['name']}\n"
        f"Возраст: {data['age']}\n"
        f"Телефон: {data['phone']}"
    )

    await state.clear()

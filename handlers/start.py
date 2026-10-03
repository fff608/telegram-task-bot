from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from handlers.keyboards import main_menu_keyboard

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}!\n\n"
        "Я — бот-задачник. Выбери, что хочешь сделать:",
        reply_markup=main_menu_keyboard(),
    )


@router.message(F.text == "ℹ️ Помощь")
async def cmd_help(message: Message):
    await message.answer(
        "Я умею:\n"
        "• 📋 Показывать список задач\n"
        "• ➕ Добавлять новые задачи\n\n"
        "Скоро научусь удалять и отмечать выполненные.",
        reply_markup=main_menu_keyboard(),
    )


@router.message(F.text == "📋 Мои задачи")
async def show_tasks(message: Message):
    await message.answer(
        "Здесь будет список твоих задач. Пока — пусто, потому что я ещё не умею их хранить.",
        reply_markup=main_menu_keyboard(),
    )


@router.message(F.text == "➕ Добавить задачу")
async def add_task(message: Message):
    await message.answer(
        "Скоро я научусь добавлять задачи. Пока — просто кнопка работает.",
        reply_markup=main_menu_keyboard(),
    )
@router.message(F.text.lower().contains("свинная туша"))
async def add_task(message: Message):
    await message.answer(
        "Сам ты свинная туша",
        reply_markup=main_menu_keyboard(),
    )
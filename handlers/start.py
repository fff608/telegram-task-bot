from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types  import CallbackQuery
from aiogram.utils import callback_answer

from handlers.keyboards import main_menu_keyboard,main_menu_inline_keyboard

router = Router()

@router.message(F.text == "📋 Мои задачи")
async def show_tasks(message: Message):
    await message.answer(
        "Выбери действие:",
        reply_markup=main_menu_inline_keyboard(),
    )


@router.callback_query(F.data=="add_task")
async def add_task(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Тут ты сможешь добавлять задачи.Скоро.")
@router.callback_query(F.data=="task_delete")
async def task_delete(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Тут ты можешь удалять задачи.")





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


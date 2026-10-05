from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types  import CallbackQuery
from aiogram.utils import callback_answer
from handlers.keyboards import main_menu_keyboard,main_menu_inline_keyboard
from aiogram.fsm.context import FSMContext
from handlers.states import TaskForm
router = Router()

@router.message(F.text == "📋 Мои задачи")
async def show_tasks(message: Message):
    await message.answer(
        "Выбери действие:",
        reply_markup=main_menu_inline_keyboard(),
    )
@router.message(Command("cancel"))
@router.message(F.text.lower() == "отмена")
async def cmd_cancel(message: Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is None:
        await message.answer("Нечего отменять.")
        return

    await state.clear()
    await message.answer(
        "❌ Действие отменено.",
        reply_markup=main_menu_keyboard(),
    )
    
@router.message(TaskForm.waiting_for_title,F.text)
async def show_tasks(message: Message,state:  FSMContext):
    title = message.text.strip()

    if not title:
        await message.answer("Название не может быть пустым,попробуй еще раз")
        return
    await state.update_data(title=title)

    await message.answer(
        f"Задача:\"{title}\" добавлена.\n\n"
    )
    reply_markup = main_menu_keyboard()
    await state.clear()



@router.callback_query(F.data=="add_task")
async def add_task(callback: CallbackQuery,state: FSMContext):
    await callback.answer()
    await callback.message.edit_text(
        "Введи название задачи:\n\n"
        "напиши /cancel чтобы отменить")
    await state.set_state(TaskForm.waiting_for_title)


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


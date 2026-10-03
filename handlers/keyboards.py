from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    """Главное меню бота."""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Мои задачи")],
            [
                KeyboardButton(text="➕ Добавить задачу"),
                KeyboardButton(text="ℹ️ Помощь"),
                KeyboardButton(text="Свинная туша"),
            ],
        ],
        resize_keyboard=True,
    )
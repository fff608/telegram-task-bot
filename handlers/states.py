from aiogram.fsm.state import State,StatesGroup
class TaskForm (StatesGroup):
    waiting_for_title = State()
import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start
from aiogram.fsm.storage.memory import MemoryStorage

async def main():
    bot = Bot(token=BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(start.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
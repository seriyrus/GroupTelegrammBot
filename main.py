import asyncio, os
from aiogram import Dispatcher, Bot, types
from dotenv import find_dotenv, load_dotenv

from handlers.user_private import user_private_router



load_dotenv(find_dotenv())

ALLOWED_UPD = ["message", "edited_message"]

bot = Bot(os.getenv("TOKEN"), parse_mode="HTML")
dp = Dispatcher()

dp.include_router(user_private_router)

async def main():
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPD)

asyncio.run(main()) 
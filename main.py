import asyncio, os
from aiogram import Dispatcher, Bot, types
from aiogram.types import BotCommandScopeAllPrivateChats
from dotenv import find_dotenv, load_dotenv
from common.bot_commands_lists import private
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router



load_dotenv(find_dotenv())

ALLOWED_UPD = ["message", "edited_message"]

bot = Bot(os.getenv("TOKEN"), parse_mode="HTML")
dp = Dispatcher()

dp.include_router(user_group_router)
dp.include_router(user_private_router)





async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope = BotCommandScopeAllPrivateChats() )
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPD)

asyncio.run(main()) 
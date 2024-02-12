import asyncio
from aiogram import Dispatcher, Bot, types
from settings import BOT_TOKEN


bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

@dp.message()
async def start_cmd(msg: types.Message):
    await msg.answer("Hello!")


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
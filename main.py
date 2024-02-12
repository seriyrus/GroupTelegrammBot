from aiogram import Dispatcher, Bot, types,F
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
import asyncio, logging
from settings import BOT_TOKEN


logging.basicConfig(level=logging.INFO)

bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()


#отправляет сообщения по команде
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello")


#Отвечает на сообщения по команде
@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
import asyncio, os
from email import message
from aiogram.filters import Command
from aiogram import Dispatcher, Bot, types
from setuptools import Command
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

bot = Bot(os.getenv("TOKEN"), parse_mode="HTML")
dp = Dispatcher()

@dp.message(message, Command("start"))
async def start_cmd(msg: types.Message):
    await msg.answer("Hello!")

@dp.message()
async def start_cmd(msg: types.Message):
    await msg.answer(msg.text)

async def main():
    await dp.start_polling(bot)

asyncio.run(main()) 
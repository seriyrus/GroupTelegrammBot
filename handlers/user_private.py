from aiogram.filters import Command
from aiogram import types, Router

user_private_router = Router()





@user_private_router.message(Command('menu'))
async def menu_cmd(msg: types.Message):
    await msg.answer("menu!")

@user_private_router.message(Command('start'))
async def start_cmd(msg: types.Message):
    await msg.answer("start!")

@user_private_router.message()
async def start_cmd(msg: types.Message):
    await msg.answer(msg.text)
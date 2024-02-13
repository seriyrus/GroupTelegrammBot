from aiogram.filters import Command, or_f
from aiogram import types, Router, F


user_private_router = Router()


@user_private_router.message(or_f(Command('menu'), F.text.lower() == "меню"))
async def menu_cmd(msg: types.Message):
    await msg.answer("Меню:")

@user_private_router.message(Command('start'))
async def start_cmd(msg: types.Message):
    await msg.answer("Здравствуйте!")

@user_private_router.message(Command('about'))
async def about_cmd(msg: types.Message):
    await msg.answer("О нас:")

@user_private_router.message(Command('payment'))
async def payment_cmd(msg: types.Message):
    await msg.answer("Оплата:")

@user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(msg: types.Message):
    await msg.answer("Доставка:")
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
    await msg.answer("бот в котором можно посмотреть актуальное расписание")

@user_private_router.message(Command('payment'))
async def payment_cmd(msg: types.Message):
    await msg.answer("пиздеж")

@user_private_router(F.text.lower().contains("команды"))
async def help(msg: types.Message):
    await msg.answer("команды:\
/start - поздороваться с ботом\
/menu - посмотреть меню\
/about - о боте\
/payment - оплата\
/shipping - доставка\
")

@user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(msg: types.Message):
    await msg.answer("на тот свет доставка бесплатная")
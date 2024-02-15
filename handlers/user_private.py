from aiogram.filters import Command, or_f
from aiogram import types, Router, F
import json, datetime 
import rasp


user_private_router = Router()
user_private_router.message.filter()


@user_private_router.message(or_f(Command('menu'), F.text.lower() == "меню"))
async def menu_cmd(msg: types.Message):
    await msg.answer("Меню:")

@user_private_router.message(Command('start'))
async def start_cmd(msg: types.Message):
    await msg.answer("Здравствуйте!")

@user_private_router.message(Command('about'))
async def about_cmd(msg: types.Message):
    about_text="""бот в котором можно посмотреть актуальное расписание,\
    текущие объявления и график дежурств!"""
    await msg.answer(about_text)

@user_private_router.message(Command('check_objavl'))
async def check_objavl_cmd(msg: types.Message):
    await msg.answer("Текущие Объявления")

@user_private_router.message(F.text.lower().contains("команды"))
async def help(msg: types.Message):
    banner = """команды: 
    /start - поздороваться с ботом 
    /menu - посмотреть меню
    /about - о боте 
    /check_rasp - посмотреть расписание 
    /check_objavl - Посмотреть объявления"""
    await msg.answer(banner)

@user_private_router.message(F.text.contains("расписание"))
@user_private_router.message(Command('check_rasp'))
async def check_rasp_cmd(msg: types.Message):
    date = datetime.datetime.now().date()
    wd = date.weekday()
    await msg.answer(rasp.create_text_rasp(wd))
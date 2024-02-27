from aiogram.filters import Command, or_f
from aiogram import types, Router, F
from filters.chat_types import ChatTypeFilter
from keyboards.reply import start_kb
import rasp
from handlers.user_group import dej_index
import datetime

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(or_f(Command('menu'), F.text.lower() == "меню"))
async def menu_cmd(msg: types.Message):
    await msg.answer("Меню:")

@user_private_router.message(Command('start'))
async def start_cmd(msg: types.Message):
    await msg.answer("Здравствуйте!", reply_markup=start_kb)

@user_private_router.message(Command('about'))
async def about_cmd(msg: types.Message):
    about_text="""бот в котором можно посмотреть актуальное расписание,\
    текущие объявления и график дежурств!"""
    await msg.answer(about_text)

@user_private_router.message(F.text.lower().contains("объявления"))
@user_private_router.message(Command('check_objavl'))
async def check_objavl_cmd(msg: types.Message):
    await msg.answer("Текущие Объявления:")

@user_private_router.message(F.text.lower().contains("расписание"))
@user_private_router.message(Command('check_rasp'))
async def check_rasp(msg: types.Message):
    date = datetime.datetime.now().date()
    wd = date.weekday()
    await msg.answer(rasp.create_text_rasp(wd,"расписание на сегодня\n"))
   
@user_private_router.message(F.text.lower().contains("дежурные"))
@user_private_router.message(Command('check_dej'))
async def check_dej(msg: types.Message):
    banner_dej = "дежурные на сегодня:\n"
    await msg.answer(rasp.create_rasp_dej(dej_index,banner_dej))    
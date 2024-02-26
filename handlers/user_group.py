from aiogram.filters import Command
from aiogram import types, Router, F
from filters.chat_types import ChatTypeFilter, restricted_words

import datetime 
import rasp
import aioschedule, asyncio

from string import punctuation


user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))

global dej_index
dej_index = 0

restricted_words = restricted_words

@user_group_router.edited_message(F.text.lower().contains("дежурств"))
@user_group_router.message(F.text.lower().contains("дежурств"))
@user_group_router.message(Command('show_dej'))
async def show_dej(msg: types.Message):
        banner_dej = "дежурные на сегодня:\n"
        await msg.answer(rasp.create_rasp_dej(dej_index,banner_dej))

def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))

async def scheduler():
    aioschedule.every().day.at("6:00").do(check_rasp_cmd)
    aioschedule.every().day.at("12:10").do(show_dej_schedule)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
        
async def on_startup(dp): 
    asyncio.create_task(scheduler())

@user_group_router.edited_message(F.text.lower().contains("расписание на завтра"))
@user_group_router.message(F.text.lower().contains("расписание на завтра"))
@user_group_router.message(Command('check_rasp_tomorrow'))
async def check_rasp_tomorrow_cmd(msg: types.Message):
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    wd = tomorrow.weekday()
    print(wd)
    await msg.answer(rasp.create_text_rasp(wd,"расписание на завтра\n"))
    


@user_group_router.edited_message(F.text.lower().contains("расписание"))
@user_group_router.message(F.text.lower().contains("расписание"))
@user_group_router.message(Command('check_rasp'))
async def check_rasp_cmd(msg: types.Message):
    date = datetime.datetime.now().date()
    wd = date.weekday()
    await msg.answer(rasp.create_text_rasp(wd,"расписание на сегодня\n"))

@user_group_router.edited_message()
@user_group_router.message()
async def start_cmd(msg: types.Message):
    if restricted_words.intersection(clean_text(msg.text.lower()).split()):
        await msg.delete()
        await msg.answer(f"{msg.from_user.first_name}, Без мата пж!")
        #await msg.chat.ban(msg.from_user.id) 



async def show_dej_schedule(msg: types.Message):
    if dej_index > 10:
        dej_index = 0
    else:
        await msg.answer(rasp.create_rasp_dej(dej_index))
        dej_index += 1
from aiogram.filters import Command
from aiogram import types, Router, F
from filters.chat_types import ChatTypeFilter

import datetime 
import rasp

from string import punctuation


user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))



restricted_words = {
'недоразвитый',"пидр", "гей","тварь",'блядь', 
'ебать', 'хуй', 'пизда', 'нахуй', 'сука', 'ебаный', 'ебучий', 'ебало', 'ебло', 
'шлюха','шалава','шлюхи','завались','блять','пидорас','еблан','ублюдок','хуесос',
'нахуя','схуяли','похую','по хую','заебало','сдохну','сдохни','сдохнуть','убейся',
'ахуе','бля','пиздос','гандон','охуел','чмо','ебал','похуй', 'пздц','пидор',
}


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))

@user_group_router.message(F.text.contains("расписание"))
@user_group_router.message(Command('check_rasp'))
async def check_rasp_cmd(msg: types.Message):
    date = datetime.datetime.now().date()
    wd = date.weekday()
    await msg.answer(rasp.create_text_rasp(wd))

@user_group_router.edited_message()
@user_group_router.message()
async def start_cmd(msg: types.Message):
    if restricted_words.intersection(clean_text(msg.text.lower()).split()):
        await msg.delete()
        await msg.answer(f"{msg.from_user.first_name}, Без мата пж!")
        #await msg.chat.ban(msg.from_user.id) 
import imp
from aiogram.filters import Command, or_f
from aiogram import types, Router, F
from string import punctuation


user_group_router = Router()


restricted_words = {'недоразвитый',"пидр", "гей","тварь",'блядь', 
'ебать', 'хуй', 'пизда', 'нахуй', 'сука', 'ебаный', 'ебучий', 'ебало', 'ебло', 
'шлюха','шалава','шлюхи','завались','блять','пидорас','еблан','ублюдок','хуесос',
'нахуя','схуяли','похую','по хую','заебало','сдохну','сдохни','сдохнуть','убейся',
'ахуе','бля','пиздос','егор','гандон','олег','макс','геля','охуел','серега','чмо','ебал','','','','','','',''
}

def clean_text(text: str):
    return text.translate(str.maketrans('','',punctuation))

@user_group_router.message()
async def start_cmd(msg: types.Message):
    if restricted_words.intersection(msg.text.lower().split()):
        await msg.delete()
        await msg.answer("Ай-ай по попке")
        #await msg.chat.ban(msg.from_user.id)
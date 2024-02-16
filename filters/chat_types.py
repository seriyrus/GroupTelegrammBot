from typing import Any
from aiogram import types
from aiogram.filters import Filter


class ChatTypeFilter(Filter):
    def __init__(self, chat_types: list[str]) -> None:
        self.chat_types = chat_types

    async def __call__(self, msg:types.Message) -> bool:
        return msg.chat.type in self.chat_types
    
restricted_words = {
'недоразвитый',"пидр", "гей","тварь",'блядь', 
'ебать', 'хуй', 'пизда', 'нахуй', 'сука', 'ебаный', 'ебучий', 'ебало', 'ебло', 
'шлюха','шалава','шлюхи','завались','блять','пидорас','еблан','ублюдок','хуесос',
'нахуя','схуяли','похую','по хую','заебало','сдохну','сдохни','сдохнуть','убейся',
'ахуе','бля','пиздос','гандон','охуел','чмо','ебал','похуй', 'пздц','пидор',
}
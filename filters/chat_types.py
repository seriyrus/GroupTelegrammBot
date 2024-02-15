from typing import Any
from aiogram import types
from aiogram.filters import Filter


class ChatTypeFilter(Filter):
    def __init__(self, chat_types: list[str]) -> None:
        self.chat_types = chat_types

    async def __call__(self, msg:types.Message) -> bool:
        return msg.chat.type in self.chat_types
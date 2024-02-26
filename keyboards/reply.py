from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



start_kb = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="Меню"),
            KeyboardButton(text="Объявления"),
            KeyboardButton(text="Расписание"),
            KeyboardButton(text="Дежурные"),
        ],
    ],
)
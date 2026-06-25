from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard: list[list[InlineKeyboardButton]] = [
    [InlineKeyboardButton(text='Дай мне цифру', callback_data='number')]
]

markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from handlers.middlewares import TestMiddleware
import random 
from keyboards.test_inline_keybord import markup as test_markup


NUMBERS = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 0
]

inline_button_router = Router()

inline_button_router.message.middleware(TestMiddleware())

#BUTTONS
button_1 = InlineKeyboardButton(text='BUTTON 1', callback_data="button_1_click")
button_2 = InlineKeyboardButton(text='BUTTON 2', callback_data='button_2_click')

#KEYBOARD
keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_1], [button_2]])


@inline_button_router.callback_query(F.data == 'number')
async def give_number_handler(callback: CallbackQuery):
    text = str(random.choice(NUMBERS))
    while text == callback.message.text:
        text = str(random.choice(NUMBERS))
    await callback.message.edit_text(
        text=text,
        reply_markup=test_markup
    )





@inline_button_router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text="Кнопка старт нажата, ниже что умеем", reply_markup=test_markup
    )

@inline_button_router.callback_query(F.data == 'button_1_click')
async def process_button_1_click(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Была нажата КНОПКА 1',
        reply_markup=callback.message.reply_markup,
        show_alert=True
    )


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data `button_2_click`
@inline_button_router.callback_query(F.data == 'button_2_click')
async def process_button_2_click(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Была нажата КНОПКА 2',
        reply_markup=callback.message.reply_markup,
        show_alert=True
    )
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton


def keyboard_registration():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [[KeyboardButton(text='Register', callback_data='button_register')],
               [KeyboardButton(text='Help', callback_data='button_help')]]
    keyboard.add(buttons)
    return keyboard

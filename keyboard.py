from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
start = types.ReplyKeyboardMarkup(resize_keyboard=True)

inform = types.KeyboardButton('Информация')
spisok = types.KeyboardButton('Список литературы для изучения Python')

start.add(inform,spisok)

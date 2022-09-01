from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from config import URL_GEO_DEC, URL_PROFKOM

from keyboards.inline.callback_datas import callback

always_choice_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn1 = types.KeyboardButton(text='Деканаты', callback_data=callback.new(
    name="decanats"
))

btn2 = types.KeyboardButton(text='Профком', callback_data=callback.new(name="profkom"))

btn3 = types.KeyboardButton(text='Расписание звонков', callback_data=callback.new(
    name="call_schedule"
))
btn4 = types.KeyboardButton(text='О нас', callback_data=callback.new(name="about"))

always_choice_1.row(btn1, btn2)
always_choice_1.row(btn3, btn4)

choice = InlineKeyboardMarkup(row_width=2)

decanat_IST = InlineKeyboardButton(text="Деканат ИСТ", callback_data=callback.new(
    name="IST"
))
choice.insert(decanat_IST)
decanat_ISP = InlineKeyboardButton(text="Деканат ИСП", callback_data=callback.new(
    name="ISP"
))
choice.insert(decanat_ISP)
cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
choice.insert(cancel_button)


decanat_geo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Посмотреть на карте", url=URL_GEO_DEC)
        ]
    ]
)

profkom_geo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Посмотреть на карте", url=URL_PROFKOM)
        ]
    ]
)

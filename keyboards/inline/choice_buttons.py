from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from references import *

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
decanat_ISP = InlineKeyboardButton(text="Деканат ИСП", callback_data=callback.new(
    name="ISP"
))
choice.add(decanat_IST, decanat_ISP)
choice.insert(InlineKeyboardButton(text="Отмена", callback_data="cancel"))


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

about = InlineKeyboardMarkup(row_width=2)
about.add(InlineKeyboardButton("VK", url=VK_IKNT), InlineKeyboardButton("Instagram", url=INST_IKNT))
about.add(InlineKeyboardButton("Сайт ИСТ", url=IST_IKNT), InlineKeyboardButton("Сайт ИСП", url=INST_IKNT))
about.add(InlineKeyboardButton("Успеваемость", url=GRADES))


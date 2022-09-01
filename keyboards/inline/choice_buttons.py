from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from references import *

from keyboards.inline.callback_datas import callback

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
dec = types.KeyboardButton(text='Деканаты', callback_data=callback.new(
    name="decanats"
))

prof = types.KeyboardButton(text='Профком', callback_data=callback.new(name="profkom"))

schedule = types.KeyboardButton(text='Расписание звонков', callback_data=callback.new(
    name="call_schedule"
))
about = types.KeyboardButton(text='О нас', callback_data=callback.new(name="about"))

keyboard.row(dec, prof)
keyboard.row(schedule, about)

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


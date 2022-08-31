from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.choice_buttons import choice, decanat_geo, always_choice_1, profkom_geo
from loader import dp


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("Что вы хотите узнать?", reply_markup=always_choice_1)


@dp.message_handler(lambda message: message.text == "Деканаты")
async def show_dec(message: types.message):
    await message.answer(text="Деканат факультета ИСТ \nДеканат факультета ИСП\nЕсли не получили необходимую информацию - нажмите отмена",
                         reply_markup=choice)



@dp.callback_query_handler(text_contains="IST")
async def info_decanat_IST(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Деканат факультета ИСТ\n"
                              "График работы: 09:00 - 16:00\n"
                              "Перерыв: 12:00 - 12:48\n"
                              "Местоположение:г.Донецк,ул.Кобозева,17 ауд.25,\n"
                              "Контактный телефон: 301-08-64\n"
                              "Почта: fist@donntu.ru\n"
                              "Telegram: https://t.me/ist_donntu", reply_markup=decanat_geo)

@dp.callback_query_handler(text_contains="ISP")
async def info_decanat_ISP(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Деканат факультета ИСП\n"
                              "График работы: 09:00 - 16:00\n"
                              "Перерыв: 12:00 - 12:48\n"
                              "Местоположение:г.Донецк,ул.Кобозева,17 ауд.27,\n"
                              "Контактный телефон:301-08-04\n"
                              "Почта: fisp@donntu.ru\n"
                              "Telegram: https://t.me/ISPstudents", reply_markup=decanat_geo)


@dp.message_handler(lambda message: message.text == "Деканаты")
async def show_dec(message: types.message):
    await message.answer(text="Деканат факультета ИСТ \nДеканат факультета ИСП\nЕсли не получили необходимую информацию - нажмите отмена",
                         reply_markup=choice)


@dp.message_handler(lambda message: message.text == "Профком")
async def show_prof(message: types.message):
    await message.answer(text="<b>1 корпус ДонНТУ ауд. 210</b> \nVK: https://vk.com/profkomstud_donntu\nInstagram/Telegram: @profkomstud_donntu\nEmail: profkomstud@donntu.org",
                         reply_markup=profkom_geo)


@dp.message_handler(lambda message: message.text == "О нас")
async def show_about(message: types.message):
    await message.answer(text="Мы в VK: https://vk.com/iknt_donntu\n"
                              "Мы в Instagram: https://instagram.com/knt_donntu\n"
                              "Сайт факультета ИСТ: http://fist.iknt.donntu.ru\n"
                              "Сайт факультета ИСП: http://fisp.iknt.donntu.ru\n"
                              "Отслеживание успеваемости: http://asu.donntu.ru",
                         reply_markup=None)


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.message.delete()


@dp.message_handler(lambda message: message.text == "Расписание звонков")
async def show_shed(message: types.message):
    await message.answer(text="<b>Понедельник - Пятница </b>\n<i>I пара  8:00 - 9:35\nII пара 9:55 - 11:30\nIII пара 11:50 - 13:25\nIV пара 13:45 - 15:20\n"
                              "V пара 15:30 - 17:05\nVI пара 17:15 - 18:50\nVII пара 19:00 - 20:35</i>\n\n"
                              "<b>Суббота - Воскресенье</b>\n<i>I пара  8:00 - 9:35\nII пара 9:45 - 11:20\nIII пара 11:40 - 13:15\nIV пара 13:25 - 15:00\n"
                              "V пара 15:10 - 16:45\nVI пара 16:55 - 18:30\nVII пара 18:40 - 20:15</i>",
                            reply_markup=None)




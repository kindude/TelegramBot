import os
from pathlib import Path

import Documentation
from Commands import Commands
from dispatcher import dp, bot
from aiogram import types
from stt import Transcriber
from DataBase import DataBase
stt = Transcriber("ru-RU")


com = Commands()

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    db = DataBase('database.db')
    com.set_user_id(message['from']['id'])
    if not db.user_exists(message["from"]["id"]):
        await bot.send_message(message.chat.id, "Я вижу вы еще не в нашей базе, сейчас мы это исправим)))")
        com.set_user_id(message['from']['id'])
        data = [message["from"]["id"], message["from"]["first_name"], message["from"]["last_name"], "25/06/2002"]
        print(db.add_user(data))
        db.add_account(message["from"]["id"])

        await bot.send_message(message.chat.id, "Теперь вы в базе!")
        await bot.send_message(message.chat.id, "Чтобы узнать правила пользования запишите голосовое сообщение : 'Правила пользования'")

    else:
        await bot.send_message(message.chat.id, "Вы уже в базе))")
        await bot.send_message(message.chat.id,
                               "Чтобы узнать правила пользования запишите голосовое сообщение : 'Правила пользования'")
    db.close()


@dp.message_handler(content_types=["voice"])
async def bot_reply_to_voice(message: types.Message):
    com.set_user_id(message['from']['id'])
    if message.content_type == types.ContentType.VOICE:
        file_id = message.voice.file_id
    elif message.content_type == types.ContentType.AUDIO:
        file_id = message.audio.file_id
    elif message.content_type == types.ContentType.DOCUMENT:
        file_id = message.document.file_id
    else:
        await message.reply("Формат документа не поддерживается")

    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_on_disk = Path("", f"{file_id}.ogg")

    await bot.download_file(file_path, destination=file_on_disk)

    print(file_on_disk)

    text = stt.transcribe(file_on_disk)
    if not text:
        text = "Не комманда"
        print(text)
    else:
        result_ = com.callback(text)
        result = f"Распознано: [{text}]\n\n" + str(result_[1])
        if result_[2] == 'documentation':
            await bot.send_message(message.chat.id, result)
        elif result_[2] in ['termsofuse', 'currency', 'None']:
            await bot.send_message(message.chat.id, result)
        elif result_[2] == "editing":
            result1 = result_[1]
            bMessage = f"Распознано: [{text}]\n\n" + str("Текущие данные аккаунта\n" + "Имя: " + result1[0][0] + "\nФамилия: " + result1[0][1] +"\n"+ "Дата рождения: " + result1[0][2])
            await bot.send_message(message.chat.id, bMessage)
        elif result_[2] == "balance":
            result1 = result_[1]
            bMessage = f"Распознано: [{text}]\n\n" + "Имя аккаунта: " + result1[0][1] + " " + result1[0][2] + "\nБаланс: " + result1[0][3] + " " + str(result1[0][4])
            await bot.send_message(message.chat.id, bMessage)
        elif result_[2] == "reference":
            result1 = result_[1]
            bMessage = f"Распознано: [{text}]\n\n" + "Дата начала акции: " + result1[0][1] + "\nДата конца акции: " + result1[0][3] + "\n" + result1[0][2]
            await bot.send_message(message.chat.id, bMessage)

        elif result_[2] == "authorization":
            sound_file = stt.create_wav(file_on_disk, stt.temp_dir)
            with open(sound_file, 'w') as file:
                # Append the content to the file
                file.write('whatever')

    # Удаление временного файла
    os.remove(file_on_disk)


@dp.message_handler(content_types=["text"])
async def bot_reply_to_text(message: types.Message):
    print(message['text'])

    if "изменить" in message['text']:
        data = message['text'].split("\n")
        data[0] = message['from']['id']
        dataPopped = data.copy()
        dataPopped = dataPopped.pop(0)
        print(dataPopped)
        com.edit(data)

        await bot.send_message(message.chat.id, message.text)
        await message.reply(message.text)

    else:
        last_message_text = message.text
        dictionary = {
            "sum": ('рубли', 'рублей'),
            "period": ('год', 'лет')
        }
        for key, values in dictionary.items():
            for value in values:
                last_message_text = last_message_text.replace(value, '')
        sum, period = last_message_text.split(',')
        dd = Documentation.create_doc(sum, period)
        await bot.send_document(message.chat.id, open(dd, 'rb'))





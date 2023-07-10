import docx
from fuzzywuzzy import fuzz
from DataBase import DataBase
from JsonParser import JsonParser
import Documentation

jsp = JsonParser()

class Commands:
    def __init__(self):

        self.opts = {
            "tbr": ('скажи', 'покажи', 'расскажи', 'сформируй'),
            "cmds": {
                "currency": ('валюты', 'валюта', 'курс', 'курс валют', 'катировки', 'котировки',),
                "balance": ('мой баланс', 'сколько у меня денег', 'баланс', 'Баланс'),
                "reference": ('справочная информация', 'доп информация', 'информация'),
                "documentation": ('документ', 'шаблонный документ', 'документация'),
                "editing": ('изменить аккаунт', 'редактировать аккаунт',),
                "termsofuse": ('правила пользования', 'правило пользования'),
                "authorization": ('авторизация'),
            }
        }


    def get_db(self):

        return self.db

    def set_user_id(self, user_id):
        self.user_id = user_id

    def callback(self, cmd):
        print(cmd)
        for x in self.opts['tbr']:
            cmd = cmd.replace(x, "").strip()
        print(cmd)
        cmd = self.recognize_cmd(cmd)
        if cmd['cmd'] != "documentation":
            result = self.execute_cmd(cmd)
        else:
            result = ["", "Уточните сумму и срок", "documentation"]

        return result

    def recognize_cmd(self, cmd):
        RC = {'cmd': 'None', 'percent': 0}
        for c, v in self.opts['cmds'].items():
            for x in v:
                vrt = fuzz.ratio(cmd, x)
                if vrt > 90:
                    if vrt > RC['percent']:
                        RC['percent'] = vrt
                        RC['cmd'] = c

        return RC

    def execute_cmd(self, cmd):

        if (cmd['cmd'] == "currency"):
            text = jsp.parse()
            return [0, text, "currency"]

        elif (cmd['cmd'] == "termsofuse"):
            return ["", "Для использования данного бота вы можете использовать несколько команд\n" \
                   "Проверка текущего баланса: Скажите 'Баланс'\n" \
                   "Курс валют: Скажите 'Валюты', 'курс валют', 'катировки'\n" \
                   "Правила пользования: Скажите:'правила пользования', 'правило пользования'\n" \
                   "Справочная информация: Скажите:'справочная информация', 'доп информация', 'информация'\n" \
                   "Формирование документации: Скажите:'документ', 'шаблонный документ', 'документация'\n" \
                   "Изменение параметров аккаунтов: Скажите:'изменить аккаунт', 'редактировать аккаунт'", "termsofuse"]

        elif (cmd['cmd'] == "balance"):
            db = DataBase('database.db')
            res = db.get_accounts(self.user_id)
            db.close()
            return["", res, "balance"]

        elif (cmd['cmd'] == "reference"):
            db = DataBase('database.db')
            res = db.get_references()

            db.close()
            return["", res, "reference"]

        elif cmd['cmd'] == "documentation":

            return [cmd['cmd'], '', "documentation"]

        elif (cmd['cmd'] == "editing"):
            db = DataBase('database.db')
            res = db.get_user(self.user_id)
            db.close()
            return ["", res, "editing"]



        elif(cmd['cmd'] == "None"):
            return [0, "Простите, я Вас не понял :(", 0]

    def edit(self, data):
        print("Hello from edit")
        db = DataBase('database.db')
        db.update_user(data)
        db.close()


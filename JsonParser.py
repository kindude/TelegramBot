import requests


class JsonParser:
    def __init__(self):
        self.API_KEY = "c85cbe13e692d2610ce105c0"
        self.urlDollar = f'https://v6.exchangerate-api.com/v6/{self.API_KEY}/pair/USD/RUB'
        self.urlEuro = f'https://v6.exchangerate-api.com/v6/{self.API_KEY}/pair/EUR/RUB'
        self.urlGBP = f'https://v6.exchangerate-api.com/v6/{self.API_KEY}/pair/GBP/RUB'

    def parse(self):
        response1 = requests.get(self.urlDollar)

        response2 = requests.get(self.urlEuro)

        response3 = requests.get(self.urlGBP)
        data1 = response1.json()
        data2 = response2.json()
        data3 = response3.json()
        time = (data1['time_last_update_utc']).replace('00:00:01 +0000', '')

        text = f"Курс валют на {time}\n" \
               f"Курс доллара: 1 ₽ = {data1['conversion_rate']} $\n" \
               f"Курс евро:  1 ₽ =  {data2['conversion_rate']} €\n" \
               f"Курс фунта стерлинга: 1 ₽ =  {data3['conversion_rate']}£\n"

        # Your JSON object
        return text


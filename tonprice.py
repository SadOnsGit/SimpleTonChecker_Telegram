from os import environ
from decimal import Decimal

import requests
import time


URL = 'https://api.coinlore.net/api/tickers/'


def send_to_telegram(message):
    url = f'https://api.telegram.org/bot{environ.get("BOT_TOKEN")}/sendMessage'
    payload = {
        'chat_id': environ.get('GROUP_CHAT_ID'),
        'text': message,
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(
            (f'Не удалось отправить сообщение в Telegram:'),
            (f'{response.status_code} - {response.text}')
        )


def GetTonPrice():
    ton_price = 0

    while True:
        response = requests.post(URL)
        if response.status_code == 200:
            data = response.json()
            for item in data['data']:
                if item['id'] == '54683':
                    new_price = Decimal(item["price_usd"])
                    message = f"TON PRICE: {new_price}"
                    if ton_price < new_price:
                        send_to_telegram(f'🟢 {message}')
                    elif ton_price > new_price:
                        send_to_telegram(f'🔴 {message}')
                    else:
                        continue
                    
                    ton_price = new_price

        else:
            print(f"Ошибка при запросе: {response.status_code}")

        time.sleep(30)

if __name__ == "__main__":
    GetTonPrice()

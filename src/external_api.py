import os

import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")
API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}


def conversion(transaction: dict) -> float | str:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    amount = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        info = response.json()
        return round(float(info["result"]), 2)
    else:
        return 0.0

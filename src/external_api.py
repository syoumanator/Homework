import os
from typing import Iterator

import requests
from dotenv import load_dotenv

# from src.utils import get_json, join_path

load_dotenv(dotenv_path="../.env")
API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}


def get_amount_rub(transactions: list, key: str = "RUB") -> Iterator:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    for transaction in transactions:
        amount = transaction.get("operationAmount", {}).get("amount")
        currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={key}&from={currency}&amount={amount}"
        if currency == key:
            yield round(float(amount), 2)
        elif currency in ["USD", "EUR"]:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                yield round(float(data["result"]), 2)
            else:
                yield 0.0
        else:
            yield 0.0


def get_list_transactions(transactions: list, len_transactions: int | str = 1) -> list:
    """Функция, которая возвращает список сумм транзакций в рублях"""
    result = get_amount_rub(transactions)
    list_transactions = [f"Сумма транзакций : {next(result)}" for _ in range(int(len_transactions))]
    return list_transactions


# if __name__ == "__main__":
#     transactions = get_json(join_path)
#     result = get_list_transactions(transactions, 1)
#     print(result)

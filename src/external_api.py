from src.utils import get_json
import requests
import os
from typing import Iterator
from dotenv import load_dotenv
load_dotenv(dotenv_path='../.env')
url = os.getenv("url")
API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}
# url = "https://api.apilayer.com/exchangerates_data/convert?to={}&from={}&amount={}"


# current_directory = os.getcwd()
# joined_path = os.path.join(current_directory, "data", "operations.json")
# print(joined_path)


def get_amount_rub(transactions: dict) -> Iterator:
    for transaction in transactions:
        amount = transaction.get("operationAmount", {}).get("amount")
        currency = transaction.get("operationAmount", {}).get("currency", {}).get('code')
        if currency == "RUB":
            yield float(amount)
        elif currency in ["USD", "EUR"]:
            response = requests.get(url.format("RUB", currency, amount), headers=headers)
            if response.status_code == 200:
                data = response.json()
                yield float(data["result"])
            else:
                yield 0.0
        else:
            yield 0.0


def trans(transactions: dict) -> list:
    result = get_amount_rub(transactions)
    list_transactions = [f'Сумма транзакций для id: {next(i['id'] for i in transactions)}: {next(result)}' for _ in range(3)]
    return list_transactions


if __name__ == "__main__":
    file_path = r"C:\Users\user\Desktop\Homework\data\operations.json"
    transactions = get_json(file_path)
    result = trans(transactions)
    print(result)


import json
from json import JSONDecodeError
from typing import Any


def get_json(file_path: str) -> Any:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            financial_transactions = json.load(file)
            return financial_transactions
    except JSONDecodeError:
        return []


# if __name__ == "__main__":
#     file_path = r"C:\Users\user\Desktop\Homework\data\operations.json"
#     transactions = get_json(file_path)
#     print(transactions)

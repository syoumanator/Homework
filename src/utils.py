import json
from json import JSONDecodeError
from pathlib import Path
from typing import Optional

from src.external_api import conversion

BASE_DIR = Path(__file__).resolve().parent.parent
join_path = BASE_DIR / "data" / "operations.json"


def get_json(file_path: Path) -> Optional[list]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                all_transactions = json.load(file)
                if isinstance(all_transactions, list):
                    return all_transactions
                else:
                    return []
            except JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


#
def get_amount_rub(transaction: dict) -> float | str:
    """Функция, которая возвращает список сумм транзакций в рублях"""
    try:
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            return float(transaction["operationAmount"]["amount"])
        else:
            return conversion(transaction)
    except KeyError:
        return "Транзакция отсутствует"

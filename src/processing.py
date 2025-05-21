import re
from collections import Counter


def filter_by_state(list_dicts: list, key: str = "EXECUTED") -> list:
    """Функция, которая принимает список словарей
    и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    return [i for i in list_dicts if i.get("state") == key.upper()]


def sort_by_date(sorted_list: list, reverse: bool = True) -> list:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date)."""
    return sorted(sorted_list, key=lambda x: x["date"], reverse=reverse)


def search_by_pattern(transactions: list, pattern: str) -> list:
    """Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""

    result = []
    for transaction in transactions:
        for val in transaction.values():
            if re.search(pattern.lower(), str(val).lower()):
                result.append(transaction)
    return result


def counter_description(transactions: list, descriptions: list) -> dict:
    """Функцию, которая принимает список словарей с данными банковских операций и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""

    result = {}
    count_description = Counter(
        item["description"] for item in transactions if item.get("description") in descriptions
    )
    for description, count in count_description.items():
        result[description] = count
    return result

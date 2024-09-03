def filter_by_state(list_data: list, key: str = "EXECUTED") -> list:
    """Функция, которая принимает список словарей
    и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    return [i for i in list_data if i["state"] == key]


def sort_by_date(sorted_list: list, reverse: bool = True) -> list:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date)."""
    return sorted(sorted_list, key=lambda x: x["date"], reverse=reverse)

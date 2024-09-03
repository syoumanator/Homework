from typing import Any, Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_num: Union[int, str]) -> Union[int, str]:
    """Функция возвращает результат обработки данных"""
    card_num_str = str(card_num)
    if card_num_str[0].lower() == "с" or len(card_num_str) == 20:
        return get_mask_account(card_num_str)
    else:
        return get_mask_card_number(card_num_str)


def get_date(date: Any) -> Any:
    """Функция возвращает дату"""
    if len(date) == 26:
        year, month, day = int(date[0:4]), int(date[5:7]), int(date[8:10])
        if 1 <= day <= 31 and 1 <= month <= 12 and year <= 2024:
            result = f"{"0" + str(day) if day < 10 else day}.{"0" + str(month) if month < 10 else month}.{year}"
            return result
    else:
        return "Некорректный ввод"

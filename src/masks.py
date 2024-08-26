from test.hidden_symbols import hidden_symbol, space
from typing import Union

user_input = input("Ввод данных пользователя: ")


def get_mask_account(user_account_numbers: Union[int, str]) -> Union[int, str]:
    """Функция возвращает замаскированный номер счёта"""
    str_user_data = str(user_account_numbers)
    list_user_data = [i for i in str_user_data]
    hidden_data = [
        list_user_data[i] if i not in range(len(list_user_data) - 20, len(list_user_data) - 4) else hidden_symbol
        for i in range(len(list_user_data))
    ]
    while hidden_data.count(hidden_symbol) != 2:
        hidden_data.remove(hidden_symbol)
    result = "".join(hidden_data)
    return result


def get_mask_card_number(card_number: Union[int, str]) -> Union[int, str]:
    """Функция возвращает замаскированный номер карты"""
    str_user_data = str(card_number)
    list_user_data = [i for i in str_user_data]
    hidden_data = [
        list_user_data[i] if i not in range(len(list_user_data) - 10, len(list_user_data) - 4) else hidden_symbol
        for i in range(len(list_user_data))
    ]
    hidden_data.insert(-4, space)
    hidden_data.insert(-9, space)
    hidden_data.insert(-14, space)
    result = "".join(hidden_data)
    return result



def length_numbers(data: Union[int, str]) -> Union[int, str]:
    """Функция проверяет длину чисел и возвращает замаскированный номер карты или счёта"""
    str_user_data = str(data)
    length_numbers = []
    list_user_data = [i for i in str_user_data]
    for i in list_user_data:
        if i.isdigit():
            length_numbers.append(i)
    if len(length_numbers) == 16:
        return get_mask_card_number(user_input)
    elif len(length_numbers) == 20:
        return get_mask_account(user_input)
    else:
        return "Некорректный ввод"


# Maestro 1596837868705199
# Счет 64686473678894779589

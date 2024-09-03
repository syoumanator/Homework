from typing import Union

space = " "
hidden_symbol = "*"


def get_mask_account(user_account_numbers: Union[int, str]) -> Union[int, str]:
    """Функция возвращает замаскированный номер счёта"""
    str_user_data = str(user_account_numbers)
    list_user_data = [i for i in str_user_data]
    list_letters = [i for i in list_user_data if i.isalpha()]
    list_numbers = [i for i in list_user_data if i.isdigit()]
    if len(list_numbers) == 20:
        hidden_data = [
            (
                list_numbers[i]
                if i not in range(len(list_numbers) - 20, len(list_numbers) - 4)
                else hidden_symbol
            )

            for i in range(len(list_numbers))
        ]
        while hidden_data.count(hidden_symbol) != 2:
            hidden_data.remove(hidden_symbol)
        result_list_numbers = "".join(hidden_data)
        result_list_letters = "".join(list_letters)
        if len(result_list_letters) > 0:
            return result_list_letters+" "+result_list_numbers
        else:
            return result_list_numbers
    else:
        return "Некорректный ввод"


def get_mask_card_number(card_number: Union[int, str]) -> Union[int, str]:
    """Функция возвращает замаскированный номер карты"""
    str_user_data = str(card_number)
    list_user_data = [i for i in str_user_data]
    list_numbers = [i for i in list_user_data if i.isdigit()]
    if len(list_numbers) == 16:
        hidden_data = [
            list_user_data[i] if i not in range(len(list_user_data) - 10, len(list_user_data) - 4) else hidden_symbol
            for i in range(len(list_user_data))
        ]
        hidden_data.insert(-4, space)
        hidden_data.insert(-9, space)
        hidden_data.insert(-14, space)
        result = "".join(hidden_data)
        return result
    else:
        return "Некорректный ввод"

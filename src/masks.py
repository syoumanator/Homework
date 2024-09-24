import logging
from typing import Union

space = " "
hidden_symbol = "*"


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/masks.log",
    filemode="w",
    encoding="utf-8",
)


account_logger = logging.getLogger(__name__)
card_logger = logging.getLogger(__name__)


def get_mask_account(user_account_numbers: Union[int, str]) -> Union[int, str]:
    """Функция возвращает замаскированный номер счёта"""
    account_logger.info("Начало маскировки счёта")
    str_user_data = str(user_account_numbers)
    list_user_data = [i for i in str_user_data]
    list_letters = [i for i in list_user_data if i.isalpha()]
    list_numbers = [i for i in list_user_data if i.isdigit()]
    if len(list_numbers) == 20:
        hidden_data = [
            (list_numbers[i] if i not in range(len(list_numbers) - 20, len(list_numbers) - 4) else hidden_symbol)
            for i in range(len(list_numbers))
        ]
        while hidden_data.count(hidden_symbol) != 2:
            hidden_data.remove(hidden_symbol)
        result_list_numbers = "".join(hidden_data)
        result_list_letters = "".join(list_letters)
        if len(result_list_letters) > 0:
            account_logger.info("Маскировка счёта прошла успешно")
            return result_list_letters + " " + result_list_numbers
        else:
            account_logger.info("Маскировка счёта прошла успешно")
            return result_list_numbers
    else:
        account_logger.warning("Маскировка счёта не удалась")
        return "Некорректный ввод"


def get_mask_card_number(card_number: Union[int, str]) -> Union[int, str]:
    """Функция возвращает замаскированный номер карты"""
    card_logger.info("Начало маскировки номера карты")
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
        card_logger.info("Маскировка номера карты прошла успешна")

        return result
    else:
        card_logger.warning("Маскировка номера карты не удалась")
        return "Некорректный ввод"

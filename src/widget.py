from typing import Union
date_input = input("Ввод данных даты: ")


def get_date(date: Union[str]) -> Union[str]:
    """Функция возвращает дату"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


print(get_date(date_input))


# Maestro 1596837868705199
# Счет 64686473678894779589

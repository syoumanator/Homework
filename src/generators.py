from typing import Iterator, List

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Функция может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    for i in range(start, stop + 1):
        numbers = "0000000000000000"
        card_number = numbers[: -len(str(i))] + str(i)
        list_card_number = [i for i in card_number]
        list_card_number.insert(-4, " ")
        list_card_number.insert(-9, " ")
        list_card_number.insert(-14, " ")
        result = "".join(list_card_number)
        yield result


def transaction_descriptions(transactions: List[dict]) -> Iterator:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    if len(transactions) > 0:
        for element in transactions:
            yield element.get("description")
    else:
        yield "Нет транзакций"


def filter_by_currency(transactions: List[dict], currency_code: str) -> Iterator:
    """Функция выдает транзакции, где валюта операции соответствует заданной."""
    if len(transactions) > 0:
        for transaction in transactions:
            if transaction.get("operationAmount", {}).get("currency", {}).get("code", {}) == currency_code:
                yield transaction
    else:
        yield "Список пустой"

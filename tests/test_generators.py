import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тестирование функции card_number_generator
def test_card_number_generator() -> None:
    number = card_number_generator(120, 121)
    assert next(number) == "0000 0000 0000 0120"


def test_card_number_generator_beginning() -> None:
    number = card_number_generator(0, 1)
    assert next(number) == "0000 0000 0000 0000"


def test_card_number_generator_end() -> None:
    number = card_number_generator(9999999999999999, 9999999999999999)
    assert next(number) == "9999 9999 9999 9999"


# Тестирование функции transaction_descriptions
def test_transaction_descriptions(transactions_information: list) -> None:
    generator = transaction_descriptions(transactions_information)
    assert next(generator) == "Перевод организации"


@pytest.mark.parametrize("index, expected", [(1, "Перевод со счета на счет"), (4, "Перевод организации")])
def test_transaction_descriptions_2(index: int, expected: str, transactions_information: list) -> None:
    descriptions = list(transaction_descriptions(transactions_information))
    assert descriptions[index] == expected


def test_transaction_descriptions_empty(test_generators_empty: list, result: str = "Нет транзакций") -> None:
    generator = transaction_descriptions(test_generators_empty)
    assert next(generator) == result


# Тестирование функции filter_by_currency
@pytest.mark.parametrize(
    "test_generators_empty, currency, expected", [([], "EUR", "Список пустой"), ([], "RUB", "Список пустой")]
)
def test_filter_by_currency_exceptions(test_generators_empty: list, currency: str, expected: str) -> None:
    generator = filter_by_currency(test_generators_empty, currency)
    assert next(generator) == expected


def test_filter_by_currency_empty(test_generators_empty: list, result: str = "Список пустой") -> None:
    generator = filter_by_currency(test_generators_empty, "USD")
    assert next(generator) == result


def test_filter_by_currency_2(transactions_information: list) -> None:
    generator = filter_by_currency(transactions_information, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_1(transactions_information: list) -> None:
    generator = filter_by_currency(transactions_information, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }

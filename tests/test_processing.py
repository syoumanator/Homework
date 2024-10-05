import pytest

from src.processing import counter_description, filter_by_state, search_by_pattern, sort_by_date


# Тестирование функции filter_by_state
def test_filter_1(test_processing: list) -> None:
    assert filter_by_state(test_processing, key="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}
    ]


def test_filter_2(test_processing: list) -> None:
    assert filter_by_state(test_processing) == [
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"}
    ]


# Тестирование функции sort_by_date
@pytest.mark.parametrize(
    "data, result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
def test_sort(data: list, result: list) -> None:
    assert sort_by_date(data) == result


def test_search_by_pattern(transactions_information: list) -> None:
    assert search_by_pattern(transactions_information, "Visa") == [
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
    assert search_by_pattern(transactions_information, "вклад") == []
    assert search_by_pattern([], "счет") == []


def test_counter_description(transactions_information: list, description_list: list) -> None:
    assert counter_description(transactions_information, description_list) == {
        "Перевод организации": 2,
        "Перевод со счета на счет": 2,
        "Перевод с карты на карту": 1,
    }
    assert counter_description([], []) == {}

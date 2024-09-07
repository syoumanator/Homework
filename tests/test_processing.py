import pytest

from src.processing import filter_by_state, sort_by_date


# Тестирование функции filter_by_state
def test_filter_1(test_processing: list) -> None:
    assert filter_by_state(test_processing, key="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}
    ]


def test_filter_2(test_processing: list) -> None:
    """Тест сверяет входные данные из conftest.py с ожидаемым результатом"""
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
    """Тест сверяет входные данные с ожидаемым результатом"""
    assert sort_by_date(data) == result

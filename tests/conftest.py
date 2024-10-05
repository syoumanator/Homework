from pathlib import Path

import pandas as pd
import pytest


@pytest.fixture
def test_processing() -> list:
    """Список входных данных"""
    return [
        {"id": 41428829, "state": 2, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "IN PROGRESS", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": " ", "date": "2018-11-14T08:21:33.419441"},
    ]


@pytest.fixture
def test_generators_empty() -> list:
    return []


@pytest.fixture
def test_generators() -> list:
    """Список входных данных"""
    return [
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


@pytest.fixture
def transaction_data_1() -> dict:
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


@pytest.fixture
def transaction_data_2() -> dict:
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def transaction_data_3() -> dict:
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def path_name() -> Path:
    return Path("test.json")


@pytest.fixture
def get_wrong_path() -> Path:
    return Path("test.jso")


@pytest.fixture
def description_list() -> list:
    return ["Перевод организации", "Перевод с карты на карту", "Перевод со счета на счет"]


@pytest.fixture
def test_df() -> pd.DataFrame:
    test_dict = {
        "date": "2023-09-05T11:30:32Z",
        "description": "Перевод организации",
        "from": "Счет 58803664561298323391",
        "id": 650703.0,
        "operationAmount": {"amount": 16210.0, "currency": {"code": "PEN", "name": "Sol"}},
        "state": "EXECUTED",
        "to": "Счет 39745660563456619397",
    }

    return pd.DataFrame(test_dict)


@pytest.fixture
def sample_data() -> dict:
    return {
        "amount": 100,
        "currency_name": "USD",
        "currency_code": "US",
        "date": "2023-01-01",
        "description": "Test transaction",
        "from": "Account A",
        "to": "Account B",
    }

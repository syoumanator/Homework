from unittest.mock import MagicMock, patch

from src.external_api import get_amount_rub, get_list_transactions, headers


def test_external_api_1(test_transactions_1: list) -> None:
    # Валюта RUB
    for transaction in test_transactions_1:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == "RUB":
            assert next(get_amount_rub(test_transactions_1)) == 31957.58


def test_external_api_2(test_transactions_2: list) -> None:
    # Валюта не RUB, USD, EUR
    for transaction in test_transactions_2:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") != "RUB" or "USD" or "EUR":
            assert next(get_amount_rub(test_transactions_2)) == 0.0


@patch("requests.get")
def test_external_api_3(mock_get: MagicMock, test_transactions_3: list) -> None:
    # Валюта USD
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": "8221.37"},
        "info": {"timestamp": 1726849624, "rate": 92.349211},
        "date": "2024-09-20",
        "result": 759222.82,
    }
    assert next(get_amount_rub(test_transactions_3)) == 759222.82
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37", headers=headers
    )


@patch("requests.get")
def test_external_api_4(mock_get: MagicMock, test_transactions_3: list) -> None:
    # Валюта USD
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": "8221.37"},
        "info": {"timestamp": 1726849624, "rate": 92.349211},
        "date": "2024-09-20",
        "result": 759222.82,
    }
    if mock_get.return_value.status_code != 200:
        assert next(get_amount_rub(test_transactions_3)) == 0.0


def test_get_list_transactions_1(transactions_list: list) -> None:
    assert get_list_transactions(transactions_list, 0) == []


def test_get_list_transactions_2(test_transactions_1: list) -> None:
    assert get_list_transactions(test_transactions_1) == ["Сумма транзакций : 31957.58"]


@patch("requests.get")
def test_get_list_transactions_3(mock_get: MagicMock, test_transactions_3: list) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": "8221.37"},
        "info": {"timestamp": 1726849624, "rate": 92.349211},
        "date": "2024-09-20",
        "result": 759222.82,
    }
    assert get_list_transactions(test_transactions_3) == ["Сумма транзакций : 759222.82"]
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37", headers=headers
    )


@patch("requests.get")
def test_get_list_transactions_4(mock_get: MagicMock, transactions_list: list) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": "8221.37"},
        "info": {"timestamp": 1726849624, "rate": 92.349211},
        "date": "2024-09-20",
        "result": 759222.82,
    }
    assert get_list_transactions(transactions_list, 2) == [
        "Сумма транзакций : 31957.58",
        "Сумма транзакций : 759222.82",
    ]
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37", headers=headers
    )

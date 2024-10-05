from unittest.mock import MagicMock, patch

from src.external_api import conversion, headers


@patch("requests.get")
def test_conversion_2(mock_get: MagicMock, transaction_data_1: dict) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": "8221.37"},
        "info": {"timestamp": 1726849624, "rate": 92.349211},
        "date": "2024-09-20",
        "result": 759222.82,
    }
    assert conversion(transaction_data_1) == 759222.82
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37", headers=headers
    )


@patch("requests.get")
def test_conversion_3(mock_get: MagicMock, transaction_data_1: dict) -> None:
    mock_get.return_value.status_code = 429
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": "8221.37"},
        "info": {"timestamp": 1726849624, "rate": 92.349211},
        "date": "2024-09-20",
        "result": 759222.82,
    }
    assert conversion(transaction_data_1) == 0.0
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37", headers=headers
    )

import json
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

from src.utils import get_amount_rub, get_json


@patch("builtins.open")
def test_get_transactions_from_json(mock_open: MagicMock, path_name: Path) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert get_json(path_name) == [{"test": "test"}]
    mock_file.read.return_value = json.dumps({})
    assert get_json(path_name) == []
    mock_file.read.return_value = json.dumps("testtest")
    assert get_json(path_name) == []
    mock_file.read.return_value = ""
    assert get_json(path_name) == []


def test_get_wrong_path(get_wrong_path: Path) -> None:
    assert get_json(get_wrong_path) == []


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
    assert get_amount_rub(transaction_data_1) == 0.0


def test_get_2(transaction_data_1: dict) -> None:
    mock_conversion = Mock(return_value=123.45)
    get_amount_rub = mock_conversion
    assert get_amount_rub(transaction_data_1) == 123.45


def test_get_3(transaction_data_2: dict) -> None:
    assert get_amount_rub(transaction_data_2) == 31957.58


def test_get_4(transaction_data_3: dict) -> None:
    assert get_amount_rub(transaction_data_3) == "Транзакция отсутствует"

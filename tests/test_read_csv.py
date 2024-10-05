from unittest.mock import MagicMock, patch

import pandas as pd

from src.read_csv import PATH_TO_CSV, read_file_csv


@patch("src.read_excel.pd.read_csv")
def test_csv(mock_read: MagicMock, test_df: pd.DataFrame) -> None:
    mock_read.return_value = test_df
    result = read_file_csv(PATH_TO_CSV)
    assert result == test_df.to_dict(orient="records")


@patch("builtins.open", side_effect=FileNotFoundError)
def test_csv_error(mock_file: MagicMock) -> None:
    result = read_file_csv(PATH_TO_CSV)
    assert result == [{}]


@patch("src.read_excel.pd.read_csv")
def test_csv_empty(mock_file: MagicMock) -> None:
    mock_file.side_effect = pd.errors.EmptyDataError
    result = read_file_csv(PATH_TO_CSV)
    assert result == [{}]


def test_transaction_csv(sample_data: dict) -> None:
    result = read_file_csv(PATH_TO_CSV)
    assert len(result) == 1000
    assert isinstance(result[0], dict)

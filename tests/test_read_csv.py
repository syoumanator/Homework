from unittest.mock import MagicMock, patch

import pandas as pd

from src.read_csv import filename, read_file_csv


@patch("src.read_csv.pd.read_csv")
def test_csv(mock_read: MagicMock, test_df: pd.DataFrame) -> None:
    mock_read.return_value = test_df
    result = read_file_csv(filename)
    assert result == test_df.to_dict(orient="records")


@patch("src.read_excel.pd.read_csv")
def test_csv_empty(mock_file: MagicMock) -> None:
    mock_file.side_effect = pd.errors.EmptyDataError
    result = read_file_csv(filename)
    assert result == [{}]


@patch("builtins.open", side_effect=Exception)
def test_csv_error(mock_file: MagicMock) -> None:
    result = read_file_csv(filename)
    assert result == [{}]

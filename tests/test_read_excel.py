from unittest.mock import MagicMock, patch

import pandas as pd

from src.read_excel import filename, read_file_excel


@patch("src.read_excel.pd.read_excel")
def test_excel(mock_read: MagicMock, test_df: pd.DataFrame) -> None:
    mock_read.return_value = test_df
    result = read_file_excel(filename)
    assert result == test_df.to_dict(orient="records")


@patch("src.read_excel.pd.read_excel")
def test_excel_empty(mock_file: MagicMock) -> None:
    mock_file.side_effect = pd.errors.EmptyDataError
    result = read_file_excel(filename)
    assert result == [{}]


@patch("builtins.open", side_effect=Exception)
def test_excel_error(mock_file: MagicMock) -> None:
    result = read_file_excel(filename)
    assert result == [{}]

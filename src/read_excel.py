import logging
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
filename = BASE_DIR / "data" / "transactions_excel.xlsx"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/read_excel.log",
    filemode="w",
    encoding="utf-8",
)


read_file_excel_logger = logging.getLogger(__name__)


def read_file_excel(filename: Path, sheet_name: int = 0) -> list:
    """Функция читает файл xlsx формата"""
    read_file_excel_logger.info(f"Чтение с файла {filename}")
    try:
        df = pd.read_excel(filename, sheet_name=sheet_name)
        read_file_excel_logger.info(f"Успешная чтение с файла {filename}")
        return df.to_dict(orient="records")
    except pd.errors.EmptyDataError as error:
        read_file_excel_logger.error(f"Произошла ошибка: {error}")
        return [{}]
    except Exception as error:
        read_file_excel_logger.error(f"Произошла ошибка: {error}")
        return [{}]

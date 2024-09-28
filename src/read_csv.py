import logging
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
filename = BASE_DIR / "data" / "transactions.csv"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/read_csv.log",
    filemode="w",
    encoding="utf-8",
)


read_file_csv_logger = logging.getLogger(__name__)


def read_file_csv(filename: Path, sep: str = ";") -> list:
    """Функция читает файл csv формата"""
    read_file_csv_logger.info(f"Чтение с файла {filename}")
    try:
        df = pd.read_csv(filename, sep=sep)
        read_file_csv_logger.info(f"Успешная чтение с файла {filename}")
        return df.to_dict(orient="records")
    except pd.errors.EmptyDataError as error:
        read_file_csv_logger.error(f"Произошла ошибка: {error}")
        return [{}]
    except Exception as error:
        read_file_csv_logger.error(f"Произошла ошибка: {error}")
        return [{}]

import logging
from pathlib import Path
from typing import Any

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
PATH_TO_CSV = BASE_DIR / "data" / "transactions.csv"
PATH_TO_EXCEL_log = BASE_DIR / "logs" / "read_csv.log"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename=PATH_TO_EXCEL_log,
    filemode="w",
    encoding="utf-8",
)


read_file_csv_logger = logging.getLogger(__name__)


def read_file_csv(path: Path, sep: str = ";") -> list[dict[Any, Any]]:
    """Функция, которая принимает на вход путь к файлу с транзакциями в формате .csv и возвращает
    список словарей с транзакциями"""
    try:
        read_file_csv_logger.info(f"Чтение файла {PATH_TO_CSV}")
        df = pd.read_csv(path, sep=sep)
        transactions = df.to_dict(orient="records")
        result = []
        for transaction in transactions:
            transaction_dict: dict[Any, Any] = {
                "id": "",
                "state": "",
                "date": "",
                "operationAmount": {"amount": "", "currency": {"name": "", "code": ""}},
                "description": "",
                "from": "",
                "to": "",
            }
            for key, value in transaction.items():
                if key == "amount":
                    transaction_dict["operationAmount"]["amount"] = value
                elif key == "currency_name":
                    transaction_dict["operationAmount"]["currency"]["name"] = value
                elif key == "currency_code":
                    transaction_dict["operationAmount"]["currency"]["code"] = value
                else:
                    transaction_dict[key] = value
            result.append(transaction_dict)
        read_file_csv_logger.info("Возврат списка словарей с транзакциями")
        return result

    except pd.errors.EmptyDataError:
        read_file_csv_logger.warning(f"Ошибка: Файл {PATH_TO_CSV} пустой.")
        return [{}]
    except FileNotFoundError:
        read_file_csv_logger.warning(f"Файл {PATH_TO_CSV} не найден.")
        return [{}]

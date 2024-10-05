import logging
from pathlib import Path
from typing import Any

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
PATH_TO_EXCEL = BASE_DIR / "data" / "transactions_excel.xlsx"
PATH_TO_EXCEL_log = BASE_DIR / "logs" / "read_excel.log"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename=PATH_TO_EXCEL_log,
    filemode="w",
    encoding="utf-8",
)


read_file_excel_logger = logging.getLogger(__name__)


def read_file_excel(path: Path, sheet_name: int = 0) -> list:
    """Функция, которая принимает на вход путь к excel-файлу с транзакциями и возвращает
    список словарей с транзакциями"""
    try:
        read_file_excel_logger.info(f"Чтение файла {PATH_TO_EXCEL}")
        df = pd.read_excel(path, sheet_name=sheet_name)
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
        read_file_excel_logger.info("Возврат списка словарей с транзакциями")
        return result

    except pd.errors.EmptyDataError:
        read_file_excel_logger.warning(f"Ошибка: Лист {sheet_name} в файле {PATH_TO_EXCEL} пустой.")
        return [{}]
    except FileNotFoundError:
        read_file_excel_logger.warning(f"Файл {PATH_TO_EXCEL} не найден.")
        return [{}]

import json
import logging
from json import JSONDecodeError
from pathlib import Path
from typing import Optional

from src.external_api import conversion

BASE_DIR = Path(__file__).resolve().parent.parent
join_path = BASE_DIR / "data" / "operations.json"


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/utils.log",
    filemode="w",
    encoding="utf-8",
)


get_json_logger = logging.getLogger(__name__)
get_amount_rub_logger = logging.getLogger(__name__)


def get_json(file_path: Path) -> Optional[list]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях."""
    get_json_logger.info("Начало считывания JSON файла")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                all_transactions = json.load(file)
                if isinstance(all_transactions, list):
                    get_json_logger.info("Начало считывания JSON файла")
                    return all_transactions
                else:
                    get_json_logger.warning("Считывание JSON файла не удалось")
                    return []
            except JSONDecodeError as error:
                get_json_logger.error(f"Произошла ошибка {error}", exc_info=True)
                return []
    except FileNotFoundError as error:
        get_json_logger.error(f"Произошла ошибка {error}", exc_info=True)
        return []


def get_amount_rub(transaction: dict) -> float | str:
    """Функция, которая возвращает результат транзакции"""
    get_amount_rub_logger.info("Начало работы с транзакциями")
    try:
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            get_amount_rub_logger.info("Транзакция уже в рублях")
            return float(transaction["operationAmount"]["amount"])
        else:
            get_amount_rub_logger.info("Перевод транзакции в рубли")
            return conversion(transaction)
    except KeyError as error:
        get_amount_rub_logger.error(f"Произошла ошибка {error}", exc_info=True)
        return "Транзакция отсутствует"

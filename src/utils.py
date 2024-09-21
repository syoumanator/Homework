import json
from json import JSONDecodeError
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).resolve().parent.parent
join_path = BASE_DIR / "data" / "operations.json"


def get_json(file_path: Path) -> Optional[list]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            all_transactions = json.load(file)
            if isinstance(all_transactions, list):
                return all_transactions
            else:
                return []
    except JSONDecodeError:
        return []


# if __name__ == "__main__":
#     result = get_json(join_path)
#     print(result)

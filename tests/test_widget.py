import pytest

from src.widget import get_date, mask_account_card


# Тестирование функции get_date
@pytest.mark.parametrize(
    "func_date_1, result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-02-12T02:26:18.671407", "12.02.2023"),
        ("2024-01-12T02:26:18.671407", "12.01.2024")
    ]
)
def test_date_1(func_date_1: str, result: str) -> None:
    """Тест сверяет входные данные с ожидаемым результатом"""
    assert get_date(func_date_1) == result


@pytest.mark.parametrize(
    "func_date_2, result",
    [
        ([], "Некорректный ввод"),
        ("20230212T02:2618.671407", "Некорректный ввод"),
        ("", "Некорректный ввод")
    ]
)
def test_date_2(func_date_2: str, result: str) -> None:
    """Тест сверяет входные данные с ожидаемым результатом"""
    assert get_date(func_date_2) == result


# Тестирование функции mask_account_card
@pytest.mark.parametrize(
    "func_mask, result",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        (" ", "Некорректный ввод"),
        (32, "Некорректный ввод"),
        ([], "Некорректный ввод")
    ]
)
def test_mask(func_mask: str, result: str) -> None:
    """Тест сверяет входные данные с ожидаемым результатом"""
    assert mask_account_card(func_mask) == result

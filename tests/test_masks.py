from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тестирование функции get_mask_account
@pytest.mark.parametrize(
    "func_acc_1, result",
    [("73654108430135874305", "**4305"), ("35383033474447895560", "**5560"), (64686473678894779589, "**9589")],
)
def test_acc_1(func_acc_1: Union[int, str], result: str) -> None:
    """Тест сверяет входные данные с ожидаемым результатом"""
    assert get_mask_account(func_acc_1) == result


@pytest.mark.parametrize(
    "func_acc_2, result",
    [("736541074305", "Некорректный ввод"), (213423, "Некорректный ввод"), ([], "Некорректный ввод")],
)
def test_acc_2(func_acc_2: Union[int, str], result: str) -> None:
    """Тест сверяет входные данные с ожидаемым результатом"""
    assert get_mask_account(func_acc_2) == result


# Тестирование функции get_mask_card_number
@pytest.mark.parametrize(
    "func_card_1, result",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("5999414228426353", "5999 41** **** 6353"),
        (8990922113665229, "8990 92** **** 5229"),
    ],
)
def test_card_1(func_card_1: Union[int, str], result: str) -> None:
    """Тест сверяет входные данные с ожидаемым результатом"""
    assert get_mask_card_number(func_card_1) == result


@pytest.mark.parametrize(
    "func_card_2, result",
    [
        ("159683786870", "Некорректный ввод"),
        (59994142, "Некорректный ввод"),
        ([], "Некорректный ввод"),
        (" ", "Некорректный ввод"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ],
)
def test_card_2(func_card_2: Union[int, str], result: str) -> None:
    """Тест сверяет входные данные с ожидаемым результатом"""
    assert get_mask_card_number(func_card_2) == result

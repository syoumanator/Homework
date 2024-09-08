import os
from typing import Any

import pytest

from src.decorators import log


def test_log() -> None:
    @log(filename="../mylog.txt")
    def example_func_1(x: int, y: int) -> int:
        return x // y

    result = example_func_1(10, 2)

    with open(os.path.join("../mylog.txt"), "rt") as file:
        for line in file:
            log_string = line

    assert log_string == "example_func_1 ok.\n"
    assert result == 5


def test_log_raise() -> None:
    @log(filename="../mylog.txt")
    def example_func_2(x: int, y: int) -> int:
        raise TypeError

    with pytest.raises(TypeError):
        example_func_2(1, 22)

    with open(os.path.join("../mylog.txt"), "rt") as file:
        for line in file:
            log_string = line

    assert log_string == "example_func_2 error: TypeError. Inputs: (1, 22), {}\n"


def test_console(capsys: Any) -> None:
    @log()
    def example_func_3(x: int, y: int) -> int:
        return x // y

    result = example_func_3(10, 2)
    captured = capsys.readouterr()

    assert captured.out == "example_func_3 ok.\n"
    assert result == 5

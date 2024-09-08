import os
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, которая логирует вызов функции
    и ее результат в файл или в консоль."""

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: tuple, **kwargs: dict) -> Any:
            log_text = ""
            try:
                result = func(*args, **kwargs)
                log_text = f"{func.__name__} ok."
                return result

            except Exception as error:
                log_text = f"{func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}"
                raise error
            finally:
                if filename:
                    with open(os.path.join(filename), "at") as file:
                        file.write(log_text + "\n")  # Запись в файл
                else:
                    print(log_text)

        return inner

    return wrapper


@log(filename="../mylog.txt")
def example_func_1(x: int, y: int) -> int:
    return x + y


example_func_1(1, 2)


# @log()
# def example_func_1(x: int, y: int) -> int:
#     return x + y
#
#
# example_func_1(1, 2)

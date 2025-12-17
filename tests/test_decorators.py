import os

import pytest

from src.decorators import log


def test_console_log(capsys):
    """Тест 1: Логи в консоль"""
    @log(filename=None)
    def add(a, b):
        return a + b

    result = add(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_file_log():
    """Тест 2: Логи в файл"""

    filename = "test_log.txt"

    # Удаляем файл, если есть
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename=filename)
    def multiply(x, y):
        return x * y

    result = multiply(3, 4)
    assert result == 12

    with open(filename, 'r') as f:
        assert "multiply ok" in f.read()

    # Удаляем файл по завершению теста
    os.remove(filename)


def test_error_console(capsys):
    """Тест 3: Ошибка в консоль"""
    @log(filename=None)
    def divide(a, b):
        return a / b

    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError" in captured.out


def test_error_file():
    """Тест 4: Ошибка в файл"""

    filename = "test_error.txt"

    if os.path.exists(filename):
        os.remove(filename)

    @log(filename=filename)
    def risky():
        raise ValueError("test")

    try:
        risky()
    except ValueError:
        pass

    with open(filename, 'r') as f:
        content = f.read()
        assert "risky error: ValueError" in content
        assert "Inputs: (), {}" in content

    os.remove(filename)

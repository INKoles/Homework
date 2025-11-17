import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(test_data, test_data_USD):
    """Тест ожидаемых значений"""
    assert list(filter_by_currency(test_data, "USD")) == test_data_USD


def test_filter_by_currency_different(test_data_USD):
    """Тест транзакции в заданной валюте отсутствуют"""
    assert list(filter_by_currency(test_data_USD, "RUB")) == []


def test_filter_by_currency_empty(test_data_description):
    """Тест с пустыми и некорректными данными"""
    assert list(filter_by_currency([], "USD")) == []
    assert list(filter_by_currency([], "")) == []
    assert list(filter_by_currency(test_data_description, "")) == []

def test_transaction_descriptions(test_data):
    """Тест ожидаемых значений"""

    assert list(transaction_descriptions(test_data)) == ["Перевод организации",
    "Перевод со счета на счет", "Перевод со счета на счет", "Перевод с карты на карту", "Перевод организации"]


def test_transaction_descriptions_empty_list(test_data_description):
    """Тест с пустым списком и разными значениями"""

    assert list(transaction_descriptions([])) == []
    assert list(transaction_descriptions(test_data_description)) == ["test1", "test3"]



def test_card_number_generator_boundaries():
    """Тест граничных значений"""

    result = list(card_number_generator(1, 1))
    assert result == ["0000 0000 0000 0001"]

    result = list(card_number_generator(9999999999999999, 9999999999999999))
    assert result == ["9999 9999 9999 9999"]


def test_card_number_generator_errors():
    """Тестируем ошибочные сценарии"""

    # start < 1
    with pytest.raises(ValueError, match="start должен быть от 1"):
        list(card_number_generator(0, 5))

    # end > 9999999999999999
    with pytest.raises(ValueError, match="end должен быть.*до 9999999999999999"):
        list(card_number_generator(9999999999999999, 10000000000000000))

    # start > end
    with pytest.raises(ValueError, match="start.*не может быть больше"):
        list(card_number_generator(10, 5))

    # Нечисловые типы
    with pytest.raises(TypeError, match="должны быть числами"):
        list(card_number_generator("abc", 5))


def test_card_number_generator_format():
    """Тестируем форматирование"""

    result = list(card_number_generator(100000000, 100000002))
    assert result[0] == "0000 0001 0000 0000"
    assert result[1] == "0000 0001 0000 0001"
    assert result[2] == "0000 0001 0000 0002"


def test_card_number_generator_large_range():
    """Тестируем большой диапазон"""
    generator = card_number_generator(9999999999999997, 9999999999999999)
    result = list(generator)

    assert len(result) == 3
    assert result[0] == "9999 9999 9999 9997"
    assert result[1] == "9999 9999 9999 9998"
    assert result[2] == "9999 9999 9999 9999"

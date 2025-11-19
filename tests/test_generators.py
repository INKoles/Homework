import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(all_transactions, usd_transactions):
    """Тест ожидаемых значений"""
    assert list(filter_by_currency(all_transactions, "USD")) == usd_transactions


def test_filter_by_currency_different(usd_transactions):
    """Тест транзакции в заданной валюте отсутствуют"""
    assert list(filter_by_currency(usd_transactions, "RUB")) == []


@pytest.mark.parametrize(
    "casual_currency", ["USD", ""]
)
def test_filter_by_currency_empty(casual_currency, casual_description):
    """Тест с пустыми и некорректными данными"""
    assert list(filter_by_currency([], casual_currency)) == []
    assert list(filter_by_currency(casual_description, "")) == []


def test_transaction_descriptions(all_transactions):
    """Тест ожидаемых значений"""

    assert list(transaction_descriptions(all_transactions)) == [
        "Перевод организации", "Перевод со счета на счет",
        "Перевод со счета на счет", "Перевод с карты на карту", "Перевод организации"]


def test_transaction_descriptions_empty_list(casual_description):
    """Тест с пустым списком и разными значениями"""

    assert list(transaction_descriptions([])) == []
    assert list(transaction_descriptions(casual_description)) == ["test1", "test3"]


@pytest.mark.parametrize(
    "start, stop, expected_num",
    [(1, 1, ["0000 0000 0000 0001"]),
     (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
     (100000000, 100000002, ["0000 0001 0000 0000", "0000 0001 0000 0001", "0000 0001 0000 0002"]),
     (9999999999999997, 9999999999999999, ["9999 9999 9999 9997", "9999 9999 9999 9998", "9999 9999 9999 9999"])
     ])
def test_card_number_generator_param(start, stop, expected_num):
    """Тестируем граничные значения, форматирование, большой диапазон"""
    result = list(card_number_generator(start, stop))
    assert result == expected_num


@pytest.mark.parametrize("start, stop, expected_exception, expected_match", [
    (0, 5, ValueError, "start должен быть от 1"),
    (10, 5, ValueError, "start.*не может быть больше"),
    ("abc", 5, TypeError, "должны быть числами"),
    (1, None, TypeError, "должны быть числами"),
    (9999999999999999, 10000000000000000, ValueError, "stop должен быть.*до 9999999999999999")
])
def test_card_number_generator_errors(start, stop, expected_exception, expected_match):
    with pytest.raises(expected_exception, match=expected_match):
        list(card_number_generator(start, stop))

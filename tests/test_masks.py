import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected_mask_card_number",
    [
        ("7000792289606361", "7000 79** **** 6361"),  # Проверка нормальной работы функции
        ("159683786870ABCD", "Некорректный номер карты"),  # В номере карты не только цифры
        ("715830073472675", "Некорректный номер карты"),  # номер карты меньше 16 цифр
    ]
)
def test_get_mask_card_number(card_number: str, expected_mask_card_number: str) -> None:
    assert get_mask_card_number(card_number) == expected_mask_card_number


@pytest.mark.parametrize(
    "account_num, expected_mask_account",
    [
        ("73654108430135874305", "**4305"),  # Проверка нормальной работы функции
        ("7365410843013587ABCD", "Некорректный номер счета"),  # В номере счёта не только цифры
        ("305", "Некорректный номер счета")  # Номер счета некорректной длины
    ]
)
def test_get_mask_account(account_num: str, expected_mask_account: str) -> None:
    assert get_mask_account(account_num) == expected_mask_account

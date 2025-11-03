import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_type_num, expected_mask_account_card",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("305", "введены некорректные данные"),
    ],
)
def test_mask_account_card(card_type_num: str, expected_mask_account_card: str) -> None:
    assert mask_account_card(card_type_num) == expected_mask_account_card


@pytest.mark.parametrize("date_input, expected_get_date", [("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_date(date_input: str, expected_get_date: str) -> None:
    assert get_date(date_input) == expected_get_date

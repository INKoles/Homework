from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_type_num: str) -> str:
    """
    Возвращает строку с замаскированным номером.
    """
    list_input = card_type_num.split(" ")

    if len(list_input[-1]) == 16 and list_input[-1].isdigit():
        return f"{" ".join(list_input[:-1])} {get_mask_card_number(list_input[-1])}"
    elif len(list_input[-1]) == 20 and list_input[-1].isdigit():
        return f"{" ".join(list_input[:-1])} {get_mask_account(list_input[-1])}"
    else:
        return "введены некорректные данные"


def get_date(date_input: str) -> str:
    """Вывод даты в корректном формате"""

    list_input = date_input.split("T")
    list_date = list_input[0].split("-")
    return ".".join(list_date[::-1])


print(mask_account_card("Счет 35383033474447895560"))
print(get_date("2024-03-11T02:26:18.671407"))

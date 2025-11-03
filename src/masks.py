def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает его маску"""

    number_to_str = str(card_number)
    if number_to_str.isdigit() and len(number_to_str) == 16:
        mask_number = number_to_str.replace(number_to_str[6:-4], "******")
        mask_card_number = " ".join(mask_number[i : i + 4] for i in range(0, len(mask_number), 4))
    else:
        return "Некорректный номер карты"
    return mask_card_number


def get_mask_account(account_num: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""

    account_num = str(account_num)
    if account_num.isdigit() and len(account_num) >= 4:
        mask_account = "**" + account_num[-4:]
    else:
        return "Некорректный номер счета"
    return mask_account

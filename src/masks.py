def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает его маску"""

    number_to_str = str(card_number)
    mask_number = number_to_str.replace(number_to_str[6:-4], "******")
    mask_card_number = " ".join(mask_number[i : i + 4] for i in range(0, len(mask_number), 4))
    return mask_card_number


def get_mask_account(account_num: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""

    mask_account = "**" + str(account_num)[-4:]
    return mask_account

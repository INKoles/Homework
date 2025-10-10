def filter_by_state(bank_operation: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """ Принимает список словарей и опционально значение для ключа
    state (по умолчанию 'EXECUTED').
    Возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению. """

    filter_tranz = []
    if not bank_operation:
        return []
    for tranz in bank_operation:
        if tranz["state"] == state:
            filter_tranz.append(tranz)
    return filter_tranz


def sort_by_date(bank_operation: list[dict], ascendig: bool = True) -> list[dict]:
    """ Принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Должна возвращать новый список, отсортированный по дате (date). """


    sorted_bank_operation = sorted(bank_operation, key=lambda x: x["date"], reverse=ascendig)
    return sorted_bank_operation


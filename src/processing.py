def filter_by_state(bank_operation: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает список словарей и опционально значение для ключа
    state (по умолчанию 'EXECUTED').
    Возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""

    transaction_filter = []
    if not bank_operation:
        return []
    for transaction in bank_operation:
        if transaction["state"] == state:
            transaction_filter.append(transaction)
    return transaction_filter


def sort_by_date(bank_operation: list[dict], sort_by_descending: bool = True) -> list[dict]:
    """Принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Должна возвращать новый список, отсортированный по дате (date)."""

    sorted_bank_operation = sorted(bank_operation, key=lambda x: x["date"], reverse=sort_by_descending)
    return sorted_bank_operation

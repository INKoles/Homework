from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> dict:
    """Принимает на вход список словарей (транзакции), возвращает итератор, который поочередно
    выдает транзакции, где валюта операции соответствует заданной (например, USD)"""

    for transaction in transactions:
        if isinstance(transaction, dict):
            if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
                yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[str, None, None]:
    """Принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""

    if not transactions:
        return

    for transaction in transactions:
        if isinstance(transaction, dict):
            description = transaction.get("description")
            if description is not None:
                yield description


def card_number_generator(start: int, end: int) -> str:
    """Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты,
     в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров."""

    try:
        start = int(start)
        end = int(end)
    except (ValueError, TypeError) as e:
        raise TypeError(f"start и end должны быть числами: {e}")

    if not (1 <= start <= 9999999999999999):
        raise ValueError(f"start должен быть от 1 до 9999999999999999, получено {start}")

    if not (1 <= end <= 9999999999999999):
        raise ValueError(f"end должен быть от 1 до 9999999999999999, получено {end}")

    if start > end:
        raise ValueError(f"start ({start}) не может быть больше end ({end})")

    current = start
    while current <= end:
        num_1 = current // 1000000000000
        num_2 = (current // 100000000) % 10000
        num_3 = (current // 10000) % 10000
        num_4 = current % 10000
        yield f"{num_1:04d} {num_2:04d} {num_3:04d} {num_4:04d}"
        current += 1

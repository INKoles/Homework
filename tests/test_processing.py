from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(bank_operation: list[dict], expected_filter_by_state_executed: list[dict]) -> None:
    """Тест с state по умолчанию ('EXECUTED')"""
    assert filter_by_state(bank_operation) == expected_filter_by_state_executed


def test_sort_by_date(bank_operation: list[dict], expected_sort_down: list[dict]) -> None:
    """ Тестирование функции сортировки даты """
    assert sort_by_date(bank_operation) == expected_sort_down

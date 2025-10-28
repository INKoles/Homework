from src.processing import filter_by_state, sort_by_date
import pytest


def test_filter_by_state_default(test_bank_operation):
    """Тест с state по умолчанию ('EXECUTED')"""
    assert filter_by_state(test_bank_operation) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]

def test_filter_by_state_canceled(test_bank_operation):
    """Тест со state='CANCELED'"""
    assert filter_by_state(test_bank_operation, "CANCELED") == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

def test_filter_by_state_canceled_2(test_bank_operation):
    """Тест с измененным регистром"""
    assert filter_by_state(test_bank_operation, "canceled") == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
def test_filter_by_state_empty():
    """Тест с пустым списком"""
    assert filter_by_state([]) == []

def test_filter_by_state_wrong_state(test_bank_operation):
    """Тест с неверным значением state"""
    assert filter_by_state(test_bank_operation, "wrong_state") == []

def test_filter_by_state_without_state(test_bank_operation_not_state):
    """Тест с входящим списком словарей без параметра state"""
    assert filter_by_state(test_bank_operation_not_state) == []

@pytest.mark.parametrize("state, expected", [
    # (state для поиска, список id которые должны быть в результате)
    ('EXECUTED', [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]),  # только EXECUTED
    ('PENDING', []),  # только PENDING
    ('CANCELED', [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]),  # несуществующий state
    (None, []),  # поиск None (ключа нет)
    ('', []),  # пустая строка
])
def test_filter_by_state_parametrize(test_bank_operation, state, expected):
    """Тестируем фильтрацию с разными состояниями"""
    result = filter_by_state(test_bank_operation, state)
    # Проверяем что получили правильные id
    assert result == expected

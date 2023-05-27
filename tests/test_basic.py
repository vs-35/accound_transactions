import pytest

from json import JSONDecodeError

from src.utils import load_operations, date_format, sorted_by_date, bank_account_hide


def test_load_operations():
    assert load_operations('data_tests/correct.json') == []

    with pytest.raises(JSONDecodeError):
        assert load_operations('data_tests/no_correct.json')

def test_date_format():
    test_date = '2018-06-30T02:08:58.425572'
    assert date_format(test_date) == '30.06.2018'


def test_sorted_by_date():
    test_date_1 = [
        {"date": "2018-08-19T04:27:37.904916"},
        {"date": "2019-09-11T17:30:34.445824"},
        {"date": "2019-07-12T08:11:47.735774"}
    ]
    assert sorted_by_date(test_date_1) == [
        {"date": "2019-09-11T17:30:34.445824"},
        {"date": "2019-07-12T08:11:47.735774"},
        {"date": "2018-08-19T04:27:37.904916"}
    ]


def test_bank_account_hide():
    test_account1 = 'Visa Classic 4195191172583802'
    assert bank_account_hide(test_account1) == 'Visa Classic 4195 19** **** 3802'
    test_account2 = 'Счет 35421428450077339637'
    assert bank_account_hide(test_account2) == 'Счет **9637'

from seasons import convert
from datetime import date, datetime

def test_convert():
    valid_test = "2022-6-18"

    assert convert("January 19, 2001") == -1
    assert convert("2900-5-23") == -1
    assert convert("1961-13-15") == -1
    assert convert("12-12-2012") == -1
    assert convert("2022-4-6 23:22:11") == -1

    assert convert(valid_test) == (date.today() - datetime.strptime(valid_test, "%Y-%m-%d").date()).total_seconds() / 60

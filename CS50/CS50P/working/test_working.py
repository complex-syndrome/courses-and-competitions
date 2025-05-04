from working import convert
import pytest

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 am to 5 pm")

def test_invalid_to():
    with pytest.raises(ValueError):
        convert("8:30 PMto10:30AM")
        convert("4:30 PM t  11:30AM")
        convert("9:30 AM to 5:30 PM")
        convert("9:00 AM - 5:00 PM")
        convert("9:00 AM -- 5:00 PM")

def test_invalid_sep():
    with pytest.raises(ValueError):
        convert("12.00 AM to 12.00 PM")
        convert("1130 AM to 1026 AM")

def test_invalid_minute():
    with pytest.raises(ValueError):
        convert("12:0 AM to 12:8 PM")
        convert("11:-1 AM to 10:5 AM")
        convert("12:00 AM to 12:70 PM")

def test_time_range():
    with pytest.raises(ValueError):
        convert("13:15 PM to 5:01 PM")
        convert("9:60 AM to 5:30 PM")
        convert("8 AM to 61.00 PM")

def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13:45 PM to 6:01 PM")
        convert("10:00 AM to 25:24 PM")

def test_time_meridiam():
    with pytest.raises(ValueError):
        convert("9 to 5")
        convert("12:00 AM to 5:00")
        convert("9:40 to 1:30AM")
        convert("9:40 to 13:30AM")


def test_output():
    assert convert("6 AM to 12 AM") == "06:00 to 00:00"
    assert convert("7:50 PM to 12 AM") == "19:50 to 00:00"
    assert convert("9 PM to 3:35 PM") == "21:00 to 15:35"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:48 PM to 12:24 AM") == "12:48 to 00:24"

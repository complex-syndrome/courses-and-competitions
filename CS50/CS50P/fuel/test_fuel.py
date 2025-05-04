from fuel import convert, gauge
from pytest import raises

def test_convert():
    with raises(ValueError):
        convert("-3/4")
        convert("7/6")
        convert("7/6")
        convert("1.3/93")
        convert("a/b")
        convert("890")


    with raises(ZeroDivisionError):
        convert("80/0")
        convert("28/0")

    assert convert("0/1") == 0
    assert convert("66/88") == 75
    assert convert("6/18") == 33
    assert convert("100/100") == 100

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(35) == "35%"
    assert gauge(72) == "72%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


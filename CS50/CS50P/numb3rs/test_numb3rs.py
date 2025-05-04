from numb3rs import validate

def test_fields():
    assert not validate("1")
    assert not validate("1.2")
    assert not validate("1.2.3")
    assert not validate("1.2.3.4.5")
    assert not validate("1.2..5")

    assert validate("1.2.3.4")


def test_numbers():
    assert not validate("1.a.4.5")
    assert not validate("b.b.b.b")
    assert not validate("1.5.6._")
    assert not validate("192.168.0.256")

    assert validate("100.255.192.172")

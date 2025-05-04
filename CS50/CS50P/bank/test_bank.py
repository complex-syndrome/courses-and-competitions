from bank import value

def test_zero():
    assert value("HElLoworld") == 0
    assert value("heLLO_") == 0
    assert value("hEllO-brain") == 0
    assert value("hELLo") == 0
    assert value("hello_world") == 0

def test_twenty():
    assert value("hewwo") == 20
    assert value("happyChar") == 20
    assert value("HA") == 20
    assert value("hBoA") == 20
    assert value("hyu") == 20

def test_hundred():
    assert value("Asparagus") == 100
    assert value("NomNom") == 100
    assert value("Cat") == 100
    assert value("WHAT") == 100
    assert value("VBS") == 100

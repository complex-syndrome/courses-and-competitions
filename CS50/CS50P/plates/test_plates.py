from plates import is_valid

def test_initial_two_letters():
    assert is_valid("he1234") == True
    assert is_valid("AB727") == True
    assert is_valid("YT923") == True
    assert is_valid("A392") == False
    assert is_valid("4RB23") == False
    assert is_valid("u2I19") == False

def test_alphanumeric():
    assert is_valid("HELLO") == True
    assert is_valid("BV839") == True
    assert is_valid("hgut3") == True
    assert is_valid("TY92_") == False
    assert is_valid("X=1") == False
    assert is_valid("A^A^2") == False

def test_length():
    assert is_valid("AS7382") == True
    assert is_valid("Pa") == True
    assert is_valid("BD72") == True
    assert is_valid("A") == False
    assert is_valid("Y") == False
    assert is_valid("UHSHH2219") == False

def test_number_not_in_middle_and_not_start_with_zero():
    assert is_valid("PO909") == True
    assert is_valid("REF678") == True
    assert is_valid("Cat") == True
    assert is_valid("A5s") == False
    assert is_valid("GH028") == False
    assert is_valid("I2O04") == False

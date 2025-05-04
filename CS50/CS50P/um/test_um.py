from um import count

def test_word_bounded():
    assert count("Umbrella") == 0
    assert count("yummy") == 0
    assert count("summation") == 0
    assert count("emu") == 0


def test_non_word_bounded():
    assert count("the-um-book") == 1
    assert count("he-um-llo?") == 1
    assert count("um?um!") == 2
    assert count("um, how do i do that?") == 1
    assert count("um..um..um..") == 3

def test_capital():
    assert count("UM") == 1
    assert count("um Um..UM..uM") == 4
    assert count("Um, are you okay") == 1

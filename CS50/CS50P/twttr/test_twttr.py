from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("BuUsl") == "Bsl"
    assert shorten("123aE") == "123"
    assert shorten("image") == "mg"
    assert shorten("oooo") == ""

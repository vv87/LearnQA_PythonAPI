def test_phrase_less_than_15_symbols():
    phrase = input("Set a phrase less than 15 symbols: ")

    assert len(phrase) < 15, "The phrase is more than 15 symbols, but needed phrase less than 15 symbols"

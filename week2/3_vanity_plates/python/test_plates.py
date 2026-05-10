from plates import plates


def test_valid_plate():
    assert plates("CS50") == 'Valid'


def test_zero_after_letters():
    assert plates("CS05") == 'Invalid'


def test_letters_after_numbers():
    assert plates("CS50P") == 'Invalid'


def test_punctuation():
    assert plates("PI3.14") == 'Invalid'


def test_too_short():
    assert plates("H") == 'Invalid'


def test_too_long():
    assert plates("OUTATIME") == 'Invalid'
    

def test_space_in_plate():
    assert plates("CS 50") == 'Invalid'
from camel import convert

def test_name():
    assert convert('name') == 'name'

def test_first_name():
    assert convert('firstName') == 'first_name'

def test_preferred_first_name():
    assert convert('preferredFirstName') == 'preferred_first_name'
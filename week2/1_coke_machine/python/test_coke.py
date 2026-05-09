from coke import coke_machine_static

def test_no_change():
    result = coke_machine_static([25, 25])
    assert result["total_inserted"] == 50
    assert result["coke_price"] == 50
    assert result["change"] == 0


def test_with_change():
    result = coke_machine_static([25, 25, 10])
    assert result["total_inserted"] == 60
    assert result["coke_price"] == 50
    assert result["change"] == 10


def test_invalid_coin():
    result = coke_machine_static([25, 25, 3, 10])
    assert result["total_inserted"] == 60
    assert result["coke_price"] == 50
    assert result["change"] == 10


def test_non_numeric_coin():
    result = coke_machine_static([25, 25, "abc", 10])
    assert result["total_inserted"] == 60
    assert result["coke_price"] == 50
    assert result["change"] == 10


def test_insufficient_funds():
    result = coke_machine_static([25, 10])
    assert result["total_inserted"] == 35
    assert result["coke_price"] == 50
    assert result["change"] == 0

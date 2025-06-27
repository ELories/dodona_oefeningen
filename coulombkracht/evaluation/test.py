
from solution import coulombkracht

def test_coulombkracht():
    assert coulombkracht(1e-6, 2e-6, 0.05) == 7.1904
    assert coulombkracht(-1e-6, 2e-6, 0.1) == 1.7976
    assert coulombkracht(3e-6, -3e-6, 0.2) == 2.0213

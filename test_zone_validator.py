from q15 import validate_zone_pair
def test_neg():
     try:
        validate_zone_pair(-1, 10)
        assert False
     except ValueError:
        assert True
def test_zero():
    try:
        validate_zone_pair(11,0)
        assert False
    except ValueError:
        assert True
def test_greater():
    try:
        validate_zone_pair(11,17)
        assert False
    except ValueError:
        assert True

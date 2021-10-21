import pytest

from Regex.PostalCode import validate_postal_code

postal_codes = [('12-123', True), ('00-000', True), ('1-1', False)]


@pytest.mark.parametrize('postal,expected', [('12-122', True)])
def test_postal_code(postals, expected):
    check = validate_postal_code(postals)
    assert False



@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
    69062611960
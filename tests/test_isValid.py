from main import isValid

# Run these tests by invoking `$ python3 -m pytest tests`
# https://docs.pytest.org/en/6.2.x/usage.html#:~:text=You%20can%20invoke%20testing%20through,the%20current%20directory%20to%20sys.


def test_valid_str_in_isValid():
    string_1 = "()"
    string_2 = "()[]{}"
    string_3 = "([])"
    assert isValid(string_1)
    assert isValid(string_2)
    assert isValid(string_3)


def test_not_valid_str_in_isValid():
    string_1 = "(]"
    string_2 = "([{})"
    string_3 = "]()"
    string_4 = "]()"

    assert not isValid(string_1)
    assert not isValid(string_2)
    assert not isValid(string_3)
    assert not isValid(string_4)

from main import is_valid_parenthesis_string

# Run these tests by invoking `$ python3 -m pytest tests`
# https://docs.pytest.org/en/6.2.x/usage.html#:~:text=You%20can%20invoke%20testing%20through,the%20current%20directory%20to%20sys.


def test_valid_str_in_is_valid_parenthesis_string():
    string_1 = "()"
    string_2 = "()[]{}"
    string_3 = "([])"
    assert is_valid_parenthesis_string(string_1)
    assert is_valid_parenthesis_string(string_2)
    assert is_valid_parenthesis_string(string_3)


def test_not_valid_str_in_is_valid_parenthesis_string():
    string_1 = "(]"
    string_2 = "([{})"
    string_3 = "]()"
    string_4 = "]()"
    string_5 = "({{]]{)]{["

    assert not is_valid_parenthesis_string(string_1)
    assert not is_valid_parenthesis_string(string_2)
    assert not is_valid_parenthesis_string(string_3)
    assert not is_valid_parenthesis_string(string_4)
    assert not is_valid_parenthesis_string(string_5)

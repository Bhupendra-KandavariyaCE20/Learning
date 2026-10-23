import pytest


from calculator import add 


@pytest.mark.parametrize(
        "a, b, expected",
        [
            (1,2,3),
            (2,5,7),
            (9, 3, 12)
        ],
        )
def test_add(a, b, expected):
    assert add(a,b) == expected


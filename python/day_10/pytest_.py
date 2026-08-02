import pytest

@pytest.fixture
def sample_user():
    return {"username": "ubuntu_dev", "role": "admin"}

def test_user_is_admin(sample_user):
    assert sample_user["role"] == "admin"


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (0, 0, 0), (-1, 1, 0)])
def test_multiple_adds(a, b, expected):
    assert a + b == expected


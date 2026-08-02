# test_math_pytest.py
def add(a, b):
    return a + b

def test_add():
    # No classes, no self.assertEqual. Just standard Python logic.
    assert add(2, 3) == 5

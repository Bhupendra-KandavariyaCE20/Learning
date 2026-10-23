import unittest


def add(a, b):
    return a+b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        # We must use self.assertEqual instead of a simple ==
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()

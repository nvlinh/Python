import unittest


class NumbersTest(unittest.TestCase):
    """Distinguishing test iterations using subtests"""
    def test_even(self):
        for i in range(6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)


if __name__ == '__main__':
    unittest.main()

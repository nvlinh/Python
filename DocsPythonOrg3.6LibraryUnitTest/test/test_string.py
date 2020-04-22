import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('NOO', 'noo'.upper())
        self.assertNotEqual('NoO', 'noo'.upper())

    def test_isupper(self):
        self.assertTrue("YES".isupper())
        self.assertFalse("yes".isupper())

    def test_split(self):
        string = 'hello test'
        self.assertEqual(string.split(), ['hello', 'test'])


if __name__ == '__main__':
    unittest.main()

import unittest


class TestStringMethods(unittest.TestCase):
    @unittest.skip("test skip")
    def test_upper(self):
        self.assertEqual('NOO', 'noo'.upper())
        self.assertNotEqual('NoO', 'noo'.upper())

    @unittest.skip("test skip")
    def test_isupper(self):
        self.assertTrue("YES".isupper())
        self.assertFalse("yes".isupper())

    @unittest.skip("test skip")
    def test_split(self):
        string = 'hello test'
        self.assertEqual(string.split(), ['hello', 'test'])


if __name__ == '__main__':
    unittest.main()

# @unittest.skip(reason)
# @unittest.skipIf(condition, reason)
# @unittest.skipUnless(condition, reason)
# @unittest.expectedFailure

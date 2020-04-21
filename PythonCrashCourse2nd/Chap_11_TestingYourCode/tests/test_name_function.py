import unittest
from name_function import get_formatted_name


class MyTestCase(unittest.TestCase):
    def test_last_first_name(self):
        """Do names like 'Linh Tam' work?"""
        full_name = get_formatted_name('linh', 'tam')
        self.assertEqual(full_name, "Linh Tam")

    def test_last_middle_first_name(self):
        """Do names likes 'Linh Nguyen Van' work?"""
        full_name = get_formatted_name('linh', 'nguyen', 'van')
        self.assertEqual(full_name, 'Linh Van Nguyen')
        self.assertNotEqual(full_name,'Nguyen Van Linh')


if __name__ == '__main__':
    unittest.main()

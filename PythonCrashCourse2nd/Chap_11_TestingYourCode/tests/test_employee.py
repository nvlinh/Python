import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee('linh', 'nguyen')

    def test_give_default_raise(self):
        """Test salary default is 23000"""
        default_salary = self.my_employee.annual_salary
        self.assertEqual(default_salary, 23000)

    def test_give_custom_raise(self):
        """Test salary raise one time is 27000"""
        self.my_employee.give_raise()
        new_salary = self.my_employee.annual_salary

        self.assertEqual(new_salary, 28000)


if __name__ == '__main__':
    unittest.main()

class Employee:
    def __init__(self, first_name, last_name, annual_salary=None):
        self.first_name = first_name
        self.last_name = last_name
        if annual_salary:
            self.annual_salary = annual_salary
        else:
            self.annual_salary = 23000


    def give_raise(self):
        self.annual_salary += 5000

class Employee:

    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, fname, lname, age, pay):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.email = fname + "." + lname + '@gmail.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
         cls.raise_amount = amount 

emp_1 = Employee('Karthik', 'Raja', 25, 50000)
emp_2 = Employee('Ajith', 'Dheiva', 25, 80000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_1.raise_amount)


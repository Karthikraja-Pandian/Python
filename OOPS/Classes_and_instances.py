
class Employee:
    
    def __init__(self, fname, lname, age, pay):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.email = fname + "." + lname + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

emp_1 = Employee('Karthik', 'Raja', 25, 50000)
emp_2 = Employee('Ajith', 'Dheiva', 25, 80000)

print(emp_1.email)

print(emp_1.fullname())
print(Employee.fullname(emp_2))
 
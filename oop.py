#Python Object Oriented Programming
class Employee:
    pass
#Instance of class
emp_1=Employee()
emp_2=Employee()
print(emp_1)
print(emp_2)

emp_1.first='Ghanshyam'
emp_1.last='Rathore'
emp_1.pay=50000

emp_2.first='Narseh'
emp_2.last='Rathore'
emp_2.pay=6000

print(emp_1.first)
print(emp_2.pay)

#__init__ function (constructor)
class employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1=employee('ghanshyam','rathore',80000)
emp_2=employee('naresh','rathore',90000)

print(emp_1.email)
print(emp_2.pay)
print(emp_1.fullname().upper())
print(employee.fullname(emp_2))

#self->instance, (first,last,pay)->Attributes, fullname()->Method


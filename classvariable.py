#class Variable
class Employee():
    raise_amount=1.04
    num_of_employees=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=self.first+'.'+self.last+'@company.com'
        Employee.num_of_employees+=1
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return false
        return true

emp_1=Employee('Ghanshyam','Rathore',60000)
emp_2=Employee('Naresh','Rathore',50000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

emp_1.raise_amount=1.05
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

print(emp_1.__dict__)
print(Employee.__dict__)

print(Employee.num_of_employees)
print(emp_1.num_of_employees)

Employee.set_raise_amount(1.05)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

emp_str1='Ghanshyam-Rathore-60000'
new_emp1=Employee.from_string(emp_str1)
print(new_emp1.first)

#print(is_workday('Monday'))
#Regular Method take instance as a first argument
#Class method take class as a first argument
#static menthod doesn't take either instance or class as a argument

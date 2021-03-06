# Python Object oriented Programming
class Employee:
	num_of_emps=0
	raise_amount=1.04
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=first+'.'+last+'@company.com'
		Employee.num_of_emps+=1
	
	def fullname(self):
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
        
        
    

emp1=Employee("Ghanshyam","Rathore",85000)
emp2=Employee("Naresh","Rathore",90000)

print(emp1.fullname())
emp
emp1.apply_raise()
print(emp1.pay)
print(emp2.email)

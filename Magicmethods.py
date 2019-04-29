#Magic Methods
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
		
	#dunder Method	
	def __repr__(self):
		return "Employe('{}','{}',{})".format(self.first,self.last,self.pay)
	#dunder Method
	def __str__(self):
	 return "{}-{}".format(self.fullname(),self.email)

	def __add__(self,other):
            return self.pay+other.pay
        
	  
emp_1=Employee('Ghanshyam','Rathore',60000)
emp_2=Employee('Naresh','Rathore',50000)
	
print(emp_1)
print(emp_2.__str__())
print(emp_2.__repr__())

#some other example of dunder method
print(int.__add__(1,2))
print(str.__add__('a','b'))

print(emp_1+emp_2)

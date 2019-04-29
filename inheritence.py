#Inheritence:creating subclasses
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
		
class developer(Employee):
	raise_amount=1.10

	def __init__(self,first,last,pay,prog_lang):

                Employee.__init__(self,first,last,pay)
                self.prog_lang=prog_lang

class manager(Employee):
        def __init__(self,first,last,pay,employees=None):

                Employee.__init__(self,first,last,pay)
                if employees is None:
                        self.employees=[]
                else:
                        self.employees=employees

        def add_emp(self,emp):
                if emp not in self.employees:
                        self.employees.append(emp)

        def remove_emp(self,emp):
                if emp in self.employees:
                        self.employees.remove(emp)

        def print_emps(self):
                for emp in self.employees:
                        print('-->',emp.fullname())
                

dev_1=developer('Ghanshyam','Rathore',60000,'Python')
dev_2=developer('Naresh','Rathore',50000,'Java')
mgr_1=manager('Hastimal','Rathore',100000,[dev_1])
print(dev_1.email)
print(dev_1.pay)

dev_1.apply_raise()
print(dev_1.pay)
#print(dev_2.pay)
print(dev_1.prog_lang)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
print(mgr_1.email)
mgr_1.print_emps()

print(isinstance(mgr_1,manager))
print(isinstance(mgr_1,Employee))
print(isinstance(mgr_1,developer))

print(issubclass(manager,Employee))
print(issubclass(developer,Employee))
print(issubclass(manager,developer))

def hello_func():
    print('Hello Python')
hello_func()

def hello_func():
    return 'hello Python'
print(hello_func())
print(hello_func().upper())

#Function with argument
def hello_func(greeting):
    return '{},Function'.format(greeting)

print(hello_func('Hi'))

#Function with default argument
def hello_func(greeting,name='You'):
    return '{},{}'.format(greeting,name)
print(hello_func('Hi'))
print(hello_func('Hi','Ghanshyam'))

#Playing with arguments
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

student_info('English','Science','Hindi',Name='Ghanshyam',Age=22,state='Rajasthan')

course=['English','Science','Hindi']
info={'Name':'Ghanshyam','Age':22,'state':'Rajasthan'}

student_info(course,info)
#To unpack the values
student_info(*course,**info)


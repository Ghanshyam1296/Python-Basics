#Conditionals and Booleans
if True:
    print('Conditonal was true')
if False:
    print('Conditional was false')

language='C++'
if language=='Python':
    print(language)
elif language=='Java':
    print(language)
else:
    print('Not Match')

a=[1,2,3]
b=[1,2,3]

#Check if a and b are same or not
print(a==b)
#check a and b has same memory location or not
print(a is b)

print(id(a))
print(id(b))
c=b
print(id(c))
print(b is c)

#is operator is equalent to
#id(a) == id(b)
# a is b



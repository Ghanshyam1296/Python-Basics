#Dictionary
student={'Name':'Ghanshyam','Age':22,'course':['Math','CompSci']}
print(student['course'])
print(student.get('Name'))
print(student.get('Age'))

student.update({'Name':'Naresh','Age':20,'phone':'02934-248277'})
print(student)

del student['Age']
print(student)

Name=student.pop('Name')
print(Name)
print(student)
#Print the number of keys in dictionary
print(len(student))
#Print the keys available in the string
print(student.keys())
#Print the value of dictionary
print(student.values())
#Print the keys and value of dictionary
print(student.items())

#Looping through dictionary
for key,value in student.items():
    print(key,value)
    

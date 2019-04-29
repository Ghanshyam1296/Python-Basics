#List, tuple & Set
#List and tuple allows to work with sequential data
#Set are unordered collection of values with no duplicate

course=['Hindi','English','Physics','Maths','Chemistry']
print(course)
print(course[0])
print(course[-2])
#Adding the element as the last value of list
course.append('Arts')
print(course)

#Adding element at specific language
course.insert(2,'Biology')
print(course)

course_2=['Economics','Accounting']
course.append(course_2)
print(course)
course.insert(0,course_2)
print(course)

#Merging two lists
course=['Hindi','English','Physics','Maths','Chemistry']
course_2=['Economics','Accounting']
course.extend(course_2)
print(course)

#Removing element from List
course.remove('Economics')
print(course)
var=course.pop()
print(var)
print(course)

#Reversing the list
course.reverse()
print(course)

#Sorting the list
course.sort()
print(course)

#Sorting Numbers
num=[5,3,2,4,1]
num.sort()
print(num)

num.sort(reverse=True)
course.sort(reverse=True)
print(num)
print(course)

#Sorted Function to return a sorted list
sorted_num=sorted(num)
print(sorted_num)

# For Loop
for i,j in enumerate(num,start=100):
    print(i,j)

for i,j in enumerate(num):
    print(i,j)

for i in enumerate(course):
    print(i)

#Converting list into delimeted string
course_str=','.join(course)
print(course_str)

#String to list conversion
new_list=course_str.split(',')
print(new_list)

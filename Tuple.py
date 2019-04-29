#List can be modified (mutable)
#Tuple can't be modified (immutable)
Tuple=('English','Hindi','Science','Maths')
Tuple_1=Tuple
print(Tuple)
print(Tuple_1)
#set
cs_course={'Science','Digital','Analog','Network'}
art_course={'Science','English','Hindi'}

print(cs_course.intersection(art_course))
print(cs_course.difference(art_course))
print(cs_course.union(art_course))

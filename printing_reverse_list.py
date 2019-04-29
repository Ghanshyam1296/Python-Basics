#Reversing the list
list=[1,2,3,4,5,6]
l=len(list)
while(l>0 ):
    l-=1
    print(list[l],end=" ")
print()
for i in range(-1,-(len(list)+1),-1):
    print(list[i],end=" ")
print()

for key, value in enumerate(list):
    print(key,value)

questions = ['name', 'colour', 'shape'] 
answers = ['apple', 'red', 'a circle']

for question,answer in zip(questions,answers):
    print(question,answer)

d={"Name":"Ghanshyam","State":"Rajasthan"}

for i,j in d.items():
    print(i,j)




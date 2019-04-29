#Array
##l=[]
##n=int(input("Enter the number of element"))
##for i in range(n):
##    x=int(input())
##    l.append(x)
##
##sum=0
##for i in l:
##    sum+=i
##print(sum)
##print(sum/len(l))

def SumList(list=[]):
    sum=0
    for i in list:
        sum+=i
    print(sum)

l=[1,2,3,4,5]
SumList(l)
        
def SumList(*args,**kwargs):
    sum=0
    for i in args:
        sum+=i
    print(sum)
    sum=0
   
    for key,value in kwargs.items():
        sum+=value
    print(sum)
        

J=(1,2,3,4,5)
SumList(1,2,3,4,5,one=1,two=2,three=3,four=4)

def SumTuple(t=()):
    sum=0
    for i in t:
        sum+=i
    print(sum)
SumTuple(J)

dict={'one':1,'two':2,'three':3,'four':4,'five':5}
def SumDict(d={}):
    sum=0
    for i in d.values():
        sum+=i
    print(sum)

SumDict(dict)

##Name='Ghanshyam Rathore'
##for i in Name:
##    print(i)

##import numpy as np
##
##arr=np.array([[1,2],[3,4]])
##print(arr)
##print(arr+arr)
##print(arr-arr)
##print(arr*arr)
##print(arr.dot(arr))
##print(arr/arr)

l=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    for j in range(3):
        print(l[i][j],end=" ")
    print()
        

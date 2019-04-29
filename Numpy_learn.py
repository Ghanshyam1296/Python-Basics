#Numpy

import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
##print(arr[0:2,::2])
index_arr=arr[[0,2],[1,2]]
##print(index_arr)
##print(arr+1)
##print(arr+arr)
##print(arr-arr)
##print(arr*arr)

a=np.array([[1.0,2,3],[3,4,5]], dtype=np.int32)
##print(a.dtype)
##print(a)
total=np.sum(a)
##print("sum=",total)

Transpose_a=a.T
##print(Transpose_a)
print("Type of array  ",type(a))
print("Dimension of array(Number of rows) ",a.ndim)
print("Size of array(number of element)  ",a.size)
print("shape of array(like(2,3)) ",a.shape)
print("Data type of array ", a.dtype)

# Array creation
#1. From List
x=np.array([[1,2,3],[4,5,6]],dtype=np.int64)
print(x)
#2. From tuple
y=np.array(((1,2,3),(4,5,6)))
print(y)

#3. Aarray of zeros and ones
p=np.zeros((2,2))
print(p)
q=np.ones((2,2))
print(p)
z=np.full((2,2),3+4j,dtype='complex')
print(z)

cond= x>1
print(x[cond])
print(y.max())
print(y.max(axis=1))#Row-wise
print(y.max(axis=0))#Column-wise
print(y.sum())
tx=x.T
print(x.dot(tx))

nsl=np.arange(1,10,1)
print(nsl)
nsl=nsl.reshape(3,3)
print(nsl)

for x in np.nditer(nsl):
    print(x)

print(np.char.lower(['GEEKS','FOR']))
print(np.char.split('geeks for geeks',sep=' '))

A=np.array([[6,1,1],[4,-2,5],[2,8,7]])
print(np.trace(A))
print(np.linalg.matrix_rank(A))
print(np.linalg.det(A))
print(np.linalg.inv(A))

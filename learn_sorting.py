#All Kinds of Sorting & searching
#Searching Method (1.Linear Search 2.Binary Search)
#1.Linear Search
l=[1,2,3,28,5,6,7,9]

def LinearSearch(seq,*args):
    for j in args:
        found=0
        for i in seq:
            if(i==j):
                found+=1
        if found==1:
            print('found')
        else:
            print('Not Found')

LinearSearch(l,10,28,4,34)

def BinarySearch(seq,v,l,r):
    if(l==r):
        return 'Not Found'
    mid=l+r//2
    if(seq[mid]==v):
        return 'Found'
    elif(seq[mid]>v):
        return BinarySearch(seq,v,l,mid)
    else:
        return BinarySearch(seq,v,mid,r)

l=[1,2,3,4,5]
print(BinarySearch(l,5,0,len(l)))

def SelectionSort(seq):
    for i in range(len(seq)):
        minpos=i
        for j in range(minpos,len(seq)):
            if seq[minpos]>seq[j]:
                (seq[minpos],seq[j])=(seq[j],seq[minpos])
    return seq
k=[3,41,2,5]
print(SelectionSort(k))
    
def BubbleSort(seq):
    for i in range(len(seq)):
        for j in range(0,len(seq)-i-1):
            if seq[j]>seq[j+1]:
                (seq[j],seq[j+1])=(seq[j+1],seq[j])
    return seq

m=[8,3,6,1]
print(BubbleSort(m))

def InsertionSort(seq):
    for i in range(len(seq)):
        sliceend=i
        while sliceend>0 and seq[sliceend]<seq[sliceend-1]:
            (seq[sliceend],seq[sliceend-1])=(seq[sliceend-1],seq[sliceend])
            sliceend-=1
    return seq
n=[45,78,23,34,56]
print(InsertionSort(n))

def partition(seq,start,end):
    pivot=seq[end]
    pindex=start
    for i in range(start,end):
        if seq[i]<=pivot:
            (seq[i],seq[pindex])=(seq[pindex],seq[i])
            pindex+=1
    (seq[pindex],seq[end])=(seq[end],seq[pindex])
    return pindex

def QuickSort(seq,start,end):
    if(start<end):
        pindex=partition(seq,start,end)
        QuickSort(seq,start,pindex-1)
        QuickSort(seq,pindex+1,end)
    return seq
o=[3,7,4,9,5,1,6,4,1,2]
print(QuickSort(o,0,len(o)-1))

def HeapSort(


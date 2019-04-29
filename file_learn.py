#File Object


"""with open('test.txt','r') as f:
    #content=f.read()
    #content=f.readlines()
    content=f.readline()
    print(content,end="")
    content=f.readline()
    print(content,end="")"""
    

"""f=open('test.txt','r')
print(f.name)
print(f.mode)"""

"""print(f.mode)
print(f.name)
print(f.closed)"""

##with open('test.txt','r') as f:
##    for line in f:
##        print(line,end="")

##print()
##with open('test.txt','r') as f:
##    size_to_read=100
##    content=f.read(size_to_read)
##    print(content,end="")
##    print(f.tell())
##    f.seek(0)
##    content=f.read(size_to_read)
##    print(content)
    
##    while(len(content)>0):
##        print(content,end="")
##        content=f.read(size_to_read)

##with open('test1.txt','w') as f:
##    f.write('Test')
##    f.seek(0)
##    #f.write('Test')
##    f.write('R')

##with open('test.txt','r') as rf:
##    with open('test_copy.txt','w') as wf:
##        for line in rf:
##            wf.write(line)

##with open('brothers.jpg','rb') as rf:
##    with open('brother_copy.jpg','wb') as wf:
##        for line in rf:
##            wf.write(line)

with open('brothers.jpg','rb') as rf:
    with open('brothers_copy.jpg','wb') as wf:
        Chunk_size=1024
        content=rf.read(Chunk_size)
        while(len(content)>0):
            wf.write(content)
            content=rf.read(Chunk_size)

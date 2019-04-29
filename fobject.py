#file Object

f=open('Desktop/fst.txt','r')

print(f.name)
print(f.mode)

f.close()

#context manager
with open('Desktop/sample.txt','r') as g:

    for line in g:
        print(line, end='')

with open('Desktop/test2.txt','w') as k:
    k.write('This the first file created using python')
    k.seek(0)
    k.write('This the first file created using python')
    
with open('Desktop/sample.txt','r') as rf:
    with open('Desktop/sample_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)

with open('Desktop/brothers.jpg','rb') as rbf:
    with open('Desktop/brothers_copy.jpg','wb') as wbf:
        for line in rbf:
            wbf.write(line)

import re
import numpy as np
input = [l.strip() for l in open('day 7\input.txt').readlines()]

files={}
current=''
i=0

while i < len(input):   
    var = input[i]
    if input[i] == '$ cd ..':
        current=current[:current.rfind('/')]
    elif input[i][:4] == '$ cd':
        current = current + '/' + input[i][5:]
        if current not in files.keys():
            files[current]=[]     

    elif input[i][:4] == '$ ls':
        pass      

    elif input[i][:3] == 'dir':
        files[current].append(current +'/'+ input[i][4:])     

    else:
        size, name = var.split (" ")
        files[current].append(int(size))
    i+=1

toremove=[]
i=0

for folder in files:
    for item in files[folder]:
        if isinstance(item, str):
            toremove.append(item)
            for n in files[item]:
                files[folder].append(n)
    for l in toremove:
        files[folder].remove(l)
    toremove=[]
    i+=1

score=0
needed = 30000000 - (70000000 - np.array(files['//']).sum())
prev=np.inf

for key in files:
    arrs=np.array(files[key]).sum()
    if arrs<=100000:
        score+=arrs
    if (arrs>=needed)&(arrs<prev):
        prev=arrs
    

print(score)
print(prev) 
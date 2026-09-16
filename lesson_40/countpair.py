n=[1,2,3,4,5,6,7]
tgt=7
left=0
right=len(n)-1
c=0
while left!=right:
    t=n[left]+n[right]
    if t==tgt:
        c=c+1
    if t>tgt:
        right=right-1
    else:
        left=left+1
    
print(c)



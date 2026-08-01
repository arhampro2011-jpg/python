nlist=[4,5,7,9,11]
left=0
right=len(nlist)-1
tgt=int(input('what is the tgt'))
inr=-1
inl=-1
while right>left:
    if nlist[right]+nlist[left]==tgt:
        inr=right
        inl=left
        break
    elif nlist[right]+nlist[left]>tgt:
        right-=1
    else:
        left+=1

if inr==-1:
    print('not found')
else:
    print(f'tgt found at {inr+1} and {inl+1}')

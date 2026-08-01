nlist=[5,17,22,33,15,2,91,6,25]
tgt=int(input('what is the target number'))
ini=-1
inj=-1
for i in range(0,len(nlist)):
    for j in range(i+1,len(nlist)):
        if nlist[i]+nlist[j]==tgt:
            inj=j
            ini=i
            break
    if inj==j:
        break

if ini==-1:
    print('tgt not found')
else:
    print(f'tgt is sum of index {ini} and index{inj}')

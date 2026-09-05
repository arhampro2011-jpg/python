n='aabbcde'
m={}
for i in n:
    if i in m:
        m[i]+=1
    else:
        m[i]=1

for i in n:
    if m[i]==1:
        print(f'the first non repeating charavter iis {i}')
        break




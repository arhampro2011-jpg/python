n=[1,-2,12,-432,21,10,-20]
m=n[0]
'''
for i in range(len(n)):
    for j in range(i,len(n)):
        sum=0
        for k in range(i,j+1):
            sum+=n[k]
        m=max(m,sum)

print(m)

for i in range(len(n)):
    sum=0
    for j in range(i,len(n)):
        sum+=n[j]
        m=max(m,sum)
'''    
csum=n[0]
for i in range(1,len(n)):
    csum=max(csum+n[i],n[i])
    m=max(m,csum)
print(m)


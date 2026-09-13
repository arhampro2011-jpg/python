n=[16,17,4,3,5,2]
# output is 17,5,2
m=[]
'''
for i in range(len(n)):
    is_less=False
    for j in range(i+1,len(n)):
        if n[i]<=n[j]:
            is_less=True
            break
    if not is_less:
        m.append(n[i])
print(m)
'''
m.append(n[-1])
cmax=n[-1]
for i in range(len(n)-2,-1,-1):
    if n[i]>cmax:
        m.append(n[i])
        cmax=n[i]
m.reverse()
print(m)


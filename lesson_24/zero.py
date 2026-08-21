n=[0,1,23,0,12,0,3,0,65]
index=0
for i in range(len(n)):
    if n[i]!=0:
        n[index]=n[i]
        index+=1

while index<len(n):
    n[index]=0
    index+=1
print(n)
    
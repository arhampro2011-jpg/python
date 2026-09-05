n=[1,2,3,4]
new=[]
prod=1
#output will be [24,12,8,6]
for i in range(len(n)):
    prod*=n[i]
for i in range (len(n)):
    n[i]=prod/n[i]

print(n)

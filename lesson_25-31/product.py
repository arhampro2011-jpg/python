n=[1,2,3,4]
new=[]
#output will be [24,12,8,6]
prod=1
for i in range(len(n)):
    for j in range(len(n)):
        if i==j:
            pass
        else:
            prod*=n[j]
    new.append(prod)
    prod=1
print(new)
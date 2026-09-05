n=[1,2,2,2,2,2,2,3]
m=[2,2,2,2,4]
a=[]
# out= 2,2

for i in n:
    if i in m:
        a.append(i)
        m.remove(i)

print(a)

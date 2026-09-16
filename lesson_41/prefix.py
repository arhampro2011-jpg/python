n=[2,4,1,5,3]
# output is 2,6, 7, 12, 15
m=n
t=0
for i in range(len(n)):
    t+=n[i]
    m[i]=t

print(m)


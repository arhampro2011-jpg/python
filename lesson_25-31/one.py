n=[1,1,1,0,1,1,1,1,0,1,0,0,1,0,0]
cmax=0
tmax=0
for i in range(len(n)):
    if n[i]==1:
        cmax+=1
        if cmax>tmax:
        tmax=cmax
    else:
        cmax=0
    

print(tmax)
    
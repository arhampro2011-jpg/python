n=[1,3,5,2,2]
'''
output is 2
'''
t=0
t=sum(n)
rsum=0
lsum=0
for i in range(len(n)):
    rsum=t-n[i]-lsum
    if rsum==lsum:
        print(i) 
        break
    else:
        lsum+=n[i]



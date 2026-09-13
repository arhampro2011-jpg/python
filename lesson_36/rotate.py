n=[1,2,3,4,5]
k=2
m=[0]*len(n)
#[4,5,1,2,3]
'''
for i in range(len(n)):
    m[i]=n[(i+k+1)%len(n)]
'''    
for i in range(len(n)):
    try:
        m[i]=n[i+k+1]
    except:
        m[i]=n[i+k+1-len(n)]

  

print(m)

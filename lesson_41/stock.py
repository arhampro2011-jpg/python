n=[7,1,5,3,6,4]
#m=[7,5,3,6,4,1]
profit=0
mini=n[0]
maxi=0
'''
for i in range(len(n)):
    for j in range(i+1,len(n)):
        profit=max(profit,n[j]-n[i])

print(profit)
'''
for i in range(len(n)):
    mini=min(mini,n[i])
    profit=n[i]-mini
    maxi=max(profit,maxi)

print(maxi)    



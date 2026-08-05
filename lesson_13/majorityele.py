n=[4,3,5,6,3,3,3,8,67,5,35,6,7,3,3,3]
hc=0
hcnum=-1

for i in range(len(n)):
    cc=0
    for j in range(len(n)):
        if n[j]==n[i]:
            cc+=1
    
    if cc>hc:
        hcnum=n[i]
        hc=cc

print(f'most frequent elemnt is {hcnum} with frequency {hc}')


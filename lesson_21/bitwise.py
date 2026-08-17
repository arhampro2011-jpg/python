n=[5,2,4,64,5,2,64]
ans=0
for i in range(len(n)):
    ans=ans^n[i]

print(ans)
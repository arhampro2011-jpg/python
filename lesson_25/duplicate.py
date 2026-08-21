n=[0,0,1,1,1,2,3,4,4,5,5,5,5,6,7,8]
i=0
while i<len(n)-1:
    if n[i]==n[i+1]:
        n.pop(i+1)
    else:
        i+=1
    


        

print(n)
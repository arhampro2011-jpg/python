height=[1,3,0,5,2,10,5]
hs=height
hs.sort()
hs.reverse()
'''
output is 6
'''
marea=max(height)

h=max(height)
for i in range(1,len(height)):
    h=hs[i]
    
    area=(i+1)*h 
    marea=max(area,marea)

print(marea)
    
    
    



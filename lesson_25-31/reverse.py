n=[2,4,6,3,5]
new=[]
#try:
#    for i in range (len(n)):
#        new.append(n[len(n)-i])
#except IndexError as e:
#    Print('index out of bounds')
#print(new)
temp=0
for i in range(len(n)//2):
    temp=n[i]
    n[i]=n[len(n)-1-i]
    n[len(n)-1-i]=temp

print(n)
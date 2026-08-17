n=[1,2,3,4,5,6,7,9,10]
total=0
for i in range(len(n)):
    total+=n[i]
x=len(n)+1
y=(x*(x+1))/2
print(f'no missing is {y-total}')


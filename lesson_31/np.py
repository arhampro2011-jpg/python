import numpy as np 
import random as ra

a=np.array([1,3,20,4,5])
b=np.array([[1,6,7],[213,25,219]])
'''
print(a)
print(type(a))
print(a[0])
print(a[1:4])

print(np.sort(a))
print(np.where(a==30))

print(a[ra.randint(0,4)])

print(b.shape)
newb=b.reshape(3,2)
print(newb)
'''

c=np.arange(2,11,dtype=np.float64).reshape(3,3)
print(c)

d=np.array([10,4,12])
print(np.add(c,d))
print(np.subtract(c,d))
print(np.multiply(c,d))
print(np.divide(c,d))
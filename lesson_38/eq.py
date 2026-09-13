import matplotlib.pyplot as plt 
import numpy as np 

x=np.arange(0,10,1)
y1=(2*x**2 +2)
y2=(2*x+1)

plt.plot(x,y1,label='2x^2 +2')
plt.plot(x,y2,label='2x+1')

plt.legend()
plt.show()



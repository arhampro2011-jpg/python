import matplotlib.pyplot as plt 

x=[1,2,3,4,5]
y1=[10,20,21,1,11]
y2=[100,50,23,99,1]

plt.plot(x,y1,linestyle='dashed',marker='o',label='q1 result')
plt.plot(x,y2,linestyle='dashed',marker='o',label='q2 result')
plt.legend()
plt.ylim(0,100)
plt.show()
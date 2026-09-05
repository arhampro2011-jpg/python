import matplotlib.pyplot as plt 

x=['mon','tue','wed','thu','fri','sat','sun']
y=[12,33,90,87,21,45,10]
plt.bar(x,y,color='red',linestyle='dashed')
plt.grid(axis='x')
plt.title('daily scores')
plt.xlabel('days')
plt.ylabel('scores')

plt.show()
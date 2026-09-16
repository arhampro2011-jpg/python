import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df=pd.read_csv('USA_Housing.csv')
corr=df.corr(numeric_only=True)
sns.heatmap(corr,annot=True, cmap='coolwarm')
plt.show()
x=[1,2,3,4,5,6,7,8,9]
y=[10,1,23,45,0,29,51,45,61]
plt.scatter(x,y,c='blue')
plt.show()

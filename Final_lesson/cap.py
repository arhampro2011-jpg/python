import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

df=pd.read_csv('heart.csv')
'''
print(df.head())

sns.barplot(data=df,x='sex',y='trestbps',hue='target')
plt.show()

print(df['target'].value_counts())
print(df['sex'].value_counts())
print(df['chol'].value_counts())
'''
sns.heatmap(data=df.corr(),annot=True,cmap='coolwarm')
plt.show()

sns.countplot(data=df,x='chol',hue='sex')
plt.show()
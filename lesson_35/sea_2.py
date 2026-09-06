import seaborn as sns 
import matplotlib.pyplot as plt 

df=sns.load_dataset('tips')
'''
sns.barplot(data=df, x='day', y='total_bill',hue='sex')
plt.xlabel('days')
plt.ylabel('bill')
plt.show()

sns.countplot(data=df, x='day',hue='sex')
plt.xlabel('days')

plt.show()

sns.boxplot(data=df, x='day', y='total_bill',hue='sex')
plt.xlabel('days')
plt.ylabel('bill')
plt.show()

sns.stripplot(data=df, x='day', y='total_bill',jitter=True)
plt.xlabel('days')
plt.ylabel('bill')
plt.show()

sns.swarmplot(data=df, x='day', y='total_bill')
plt.xlabel('days')
plt.ylabel('bill')
plt.show()

sns.jointplot(data=df, x='day', y='total_bill')
plt.xlabel('days')
plt.ylabel('bill')
plt.show()

sns.jointplot(data=df, x='tip', y='total_bill', kind='kde')
plt.xlabel('days')
plt.ylabel('bill')
plt.show()

sns.pairplot(df[['total_bill','tip','size']])
plt.xlabel('days')
plt.ylabel('bill')
plt.show()

sns.pointplot(data=df, x='day', y='total_bill',hue='sex')
plt.xlabel('days')
plt.ylabel('bill')
plt.show()
'''
sns.lmplot(data=df, x='tip', y='total_bill',hue='sex')
plt.xlabel('days')
plt.ylabel('bill')
plt.show()
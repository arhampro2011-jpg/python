import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df=pd.read_csv('country_vaccinations.csv')

print(df.head(10))
df.isnull().any()
print(df.isnull().sum())
sub=df.iloc[0:100,:]
'''
sns.heatmap(df.isnull(),cmap='viridis',cbar=False)
plt.show()



sns.heatmap(dfclean.isnull(),cmap='viridis',cbar=False)
plt.show()
'''
dfclean=df.dropna()
print(len(df))
print(len(dfclean))
import seaborn as sns 
import matplotlib.pyplot as plt

df=sns.load_dataset('penguins')
df=df.dropna()

print(df)
sns.histplot(data=df, x='bill_length_mm',color='steelblue',bins=20,kde=True)
plt.title('bill')
plt.xlabel('mm')
plt.show()
'''
sns.kdeplot(data=df, x='flipper_length_mm', fill=True, hue='species')
plt.show()
'''
sns.scatterplot(data=df,x='flipper_length_mm',y='body_mass_g',hue='species')
plt.show()

corr=df.corr(numeric_only=True)
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.show()
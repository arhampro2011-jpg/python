import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

df=sns.load_dataset('penguins')

sns.barplot(data=df, x='island', hue='sex',y='bill_length_mm')
plt.show()
sns.swarmplot(data=df, x='island',y='bill_length_mm')
plt.show()
sns.joinplot(data=df,x='island',y='bill_length_mm')
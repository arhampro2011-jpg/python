import matplotlib.pyplot as plt 
import pandas as pd 

df=pd.read_csv('countries.csv')
c_52=df.loc[df['year']==1952]
c_07=df.loc[df['year']==2007]
print(c_52.head())
print(c_07.head())
c_merge=c_52.merge(c_07,left_on='country',right_on='country')

c_merge.drop(['year_x','year_y'],axis=1)
c_merge['popg']=c_merge['population_y']-c_merge['population_x']
print(c_merge.head())

c_merge.sort_values('popg',ascending=False).head(10)
c=['China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Bangladesh', 'Nigeria', 'Mexico', 'Philippines']
pop_g=(c_merge['popg'])/10**7

plt.bar(c,pop_g)

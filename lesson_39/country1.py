
import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv('countries.csv')

c_52 = df.loc[df['year'] == 1952]

c_07 = df.loc[df['year'] == 2007]

c_merge = c_52.merge(

c_07,

left_on='country',

right_on='country'

)

c_merge = c_merge.drop(['year_x', 'year_y'], axis=1)

c_merge['pop'] = c_merge['population_y'] - c_merge['population_x']

c_merge = c_merge.sort_values('pop', ascending=False).head(10)

names = [

'China', 'India', 'United States', 'Indonesia', 'Brazil',

'Pakistan', 'Bangladesh', 'Nigeria', 'Mexico', 'Philippines'

]

pop_g = c_merge['pop'] / 10**7

plt.bar(names, pop_g)

plt.xticks(rotation=45)

plt.show()
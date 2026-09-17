import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('imdb_top_1000.csv')

# 1 n 2
print(df.head(3))
print(df.tail(3))

# 3
df.info()

# 4 nulls
print(df.isnull().sum())

# 5 subset
sub = df.iloc[41:76]
print(sub)

# 6 highest votes
# string or int? 
print(df[df['No_of_Votes'] == df['No_of_Votes'].max()])

# clean runtime string so plot doesnt break
df['Runtime'] = df['Runtime'].str.replace(' min', '').astype(float)

# 7 boxplots
plt.figure()
plt.subplot(1, 2, 1)
sns.boxplot(y=df['IMDB_Rating'])

plt.subplot(1, 2, 2)
sns.boxplot(y=df['Runtime'])
plt.show()

# 8 rating vs runtime
plt.scatter(df['Runtime'], df['IMDB_Rating'])
plt.xlabel('Runtime')
plt.ylabel('Rating')
plt.show()

# 9 dist
plt.figure()
plt.subplot(1, 2, 1)
sns.histplot(df['IMDB_Rating'])

plt.subplot(1, 2, 2)
sns.histplot(df['Runtime'])
plt.show()

# 10 countplot
sns.countplot(x='IMDB_Rating', data=df)
plt.xticks(rotation=90)
plt.show()
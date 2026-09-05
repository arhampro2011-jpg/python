import pandas as pd 

scores=[20,30,32,40,21]
pscore= pd.Series(scores, index =['a','b','c','d','e'])
print(scores)
print(pscore)

players={
    'age':[21,12,22,13],
    'name':['a','b','c','d'],
    'score':[200,300,150,450]

}
print(players)
pdplayers=pd.DataFrame(players)
'''
print(pdplayers)
print(pdplayers.loc[0])
print(pdplayers.head())
print(pdplayers.tail())
print(pdplayers.info())
'''
a=pd.read_csv('student_data_dirty.csv')
print(a)
b=a.drop_duplicates()
print(b)
c=b.dropna()
print(c)
c['Age']=pd.to_numeric(c['Age'],errors='coerce')
print(c)
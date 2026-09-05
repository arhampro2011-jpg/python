import sqlite3
import pandas as pd

conn=sqlite3.connect('cities.db')

conn.execute('''
create table if not exists city(
city_id text primary key,
name text unique not null,
capital text default 'no',
population int );
''')

conn.commit()
try:
    conn.execute('''
    insert into city values 
    ('1','mumbai',null,10000000),
    ('2','delhi','yes',15000000),
    ('3','tokyo','yes',210000000),
    ('4','bangkok','yes',30000000);
    ''')
    print('data added')

    conn.commit()
except:
    conn.rollback()






try:
    conn.execute('''insert into city (city_id, name)
    values ('5','mumbai')''')
    conn.commit()
except sqlite3.IntegrityError as e:
    conn.rollback()
    print('rejected',e)

city =pd.read_sql('select * from city',conn)
print(city)
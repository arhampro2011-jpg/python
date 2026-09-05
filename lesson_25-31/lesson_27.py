import sqlite3
import pandas as pd 

conn=sqlite3.connect('database.sqlite')

q1=pd.read_sql('''select  count(*) as no_of_16
from students
where age=16;''',conn)

q1=pd.read_sql('''select  avg(age) as avg_age
from students;''',conn)

q1=pd.read_sql('''select  count(*) as no_of_ages, age, name
from students
group by age;''',conn)

q1=pd.read_sql('''select  * 
from students
order  by student_id desc limit 3;''',conn)

print(q1)
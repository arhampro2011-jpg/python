import sqlite3
import pandas as pd 

conn=sqlite3.connect('database.sqlite')

q1=pd.read_sql('''select *
from students;''',conn)
#print(q1)

q1=pd.read_sql('''select *
from students
where age between 10 and 20;''',conn)
#print(q1)

q1=pd.read_sql('''select *
from students
where age=16 and city in ('Mumbai','Nagpur');''',conn)
#print(q1)

q1=pd.read_sql('''select *
from students
where name like '%u%';''',conn)
#print(q1)

q1=pd.read_sql('''select min(age) as min_age, max(age) as max_age
from students;''',conn)
print(q1)

# student_id   name  age    city
#0           1  Rahul   16    Pune
#1           2  Priya   17  Mumbai
#2           3   Amit   16  Nagpur
#3           4  Sneha   17    Pune
#4           5  Arjun   16  Nashik
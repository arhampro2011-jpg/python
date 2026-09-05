import sqlite3
import pandas as pd

conn=sqlite3.connect('database.sqlite')
table=pd.read_sql('select * from sqlite_master;',conn)

print(table)
students=pd.read_sql('select * from students;',conn)
print(students)
import sqlite3

import pandas as pd

# ---- PART 1: Build and Explore the Tables ----

conn = sqlite3.connect('recipe.db')

conn.execute("CREATE TABLE if not exists recipe (recipe_id INTEGER PRIMARY KEY, recipe_name TEXT NOT NULL, cuisine TEXT NOT NULL, prep_mins INTEGER NOT NULL)")
conn.execute("CREATE TABLE if not exists ingredient (ingredient_id INTEGER PRIMARY KEY, recipe_id INTEGER NOT NULL, item TEXT NOT NULL, quantity_g INTEGER NOT NULL)")
try:
    conn.executemany("INSERT INTO recipe VALUES (?, ?, ?, ?)", [

    (1, 'Pasta', 'Italian', 20),

    (2, 'Tacos', 'Mexican', 15),

    (3, 'Sushi', 'Japanese', 45),

    (4, 'Pizza', 'Italian', 30),

    (5, 'Salad', 'Greek', 10),

    ])

    conn.executemany("INSERT INTO ingredient VALUES (?, ?, ?, ?)", [

    (1, 1, 'Pasta', 200),

    (2, 1, 'Sauce', 150),

    (3, 2, 'Tortilla', 80),

    (4, 2, 'Beef', 120),

    (5, 3, 'Salmon', 180),

    (6, 4, 'Dough', 250),

    (7, 5, 'Lettuce', 50),

    (8, 5, 'Feta', 40),
    ])
    conn.commit()
except:
    conn.rollback()
q1=pd.read_sql('''select * from recipe''',conn)


q1=pd.read_sql('select recipe_id as recipe_no,recipe_name as dish, cuisine as style, prep_mins as time from recipe',conn)

q1=pd.read_sql('select * from recipe as r left join ingredient as i on r.recipe_id =i.recipe_id',conn)

q1=pd.read_sql('select recipe_name ,cuisine from recipe where recipe_id in (select recipe_id from ingredient where quantity_g >100)',conn)
q1=pd.read_sql('select * from recipe where prep_mins=(select min(prep_mins) from recipe)',conn)
q1=pd.read_sql('select * from recipe where prep_mins=(select max(prep_mins) from recipe)',conn)
print(q1)








'''
   recipe_id recipe_name   cuisine  prep_mins
0          1       Pasta   Italian         20
1          2       Tacos   Mexican         15
2          3       Sushi  Japanese         45
3          4       Pizza   Italian         30
4          5       Salad     Greek         10
   ingredient_id  recipe_id      item  quantity_g
0              1          1     Pasta         200
1              2          1     Sauce         150
2              3          2  Tortilla          80
3              4          2      Beef         120
4              5          3    Salmon         180
5              6          4     Dough         250
6              7          5   Lettuce          50
7              8          5      Feta          40
'''
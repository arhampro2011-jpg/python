import sqlite3
import pandas as pd
conn = sqlite3.connect('book.db')

conn.execute("""CREATE TABLE if not exists author (
author_id INTEGER PRIMARY KEY,
author_name TEXT NOT NULL UNIQUE
)""")

conn.execute("""CREATE TABLE if not exists book (
book_id INTEGER PRIMARY KEY,
book_title TEXT NOT NULL,

author_id INTEGER

)""")
try:
    conn.executemany("INSERT INTO author VALUES (?, ?)", [

    (1, 'Roald Dahl'), (2, 'J.K. Rowling'),

    (3, 'Rick Riordan'), (4, 'Jeff Kinney'),

    (5, 'Dav Pilkey'), (6, 'Lemony Snicket'),

    ])
    conn.commit()
except:
    conn.rollback()

try:
    conn.executemany("INSERT INTO book VALUES (?, ?, ?)", [

    (1, 'Charlie and the Chocolate Factory', 1),

    (2, 'James and the Giant Peach', 1),

    (3, 'Harry Potter and the Philosophers Stone', 2),

    (4, 'Harry Potter and the Chamber of Secrets', 2),

    (5, 'The Lightning Thief', 3),

    (6, 'The Sea of Monsters', 3),

    (7, 'Diary of a Wimpy Kid', 4),

    ])
    conn.commit()
except:
    conn.rollback()



authors = pd.read_sql("SELECT * FROM author", conn)

books = pd.read_sql("SELECT * FROM book", conn)

#print(authors)

#print(books)
q1=pd.read_sql('select a.author_id, b.book_title, a.author_name from author as a join book as b on a.author_id=b.author_id;',conn)


q1=pd.read_sql('select a.author_id, b.book_title, a.author_name from author as a left join book as b on a.author_id=b.author_id;',conn)


q1=pd.read_sql('select a.author_id, b.book_title, a.author_name from author as a cross join book as b;',conn)

q1=pd.read_sql('select author_id,author_name from author union select book_id,book_title from book;',conn)

print(q1)

'''   author_id     author_name
0          1      Roald Dahl
1          2    J.K. Rowling
2          3    Rick Riordan
3          4     Jeff Kinney
4          5      Dav Pilkey
5          6  Lemony Snicket
   book_id                               book_title  author_id
0        1        Charlie and the Chocolate Factory          1
1        2                James and the Giant Peach          1
2        3  Harry Potter and the Philosophers Stone          2
3        4  Harry Potter and the Chamber of Secrets          2
4        5                      The Lightning Thief          3
5        6                      The Sea of Monsters          3
6        7                     Diary of a Wimpy Kid          4
'''
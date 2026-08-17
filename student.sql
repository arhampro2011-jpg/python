create table students(
  studentno INt,
  name varchar(255),
  marks decimal(5,2),
  city varchar(255)
 );
 insert into students(studentno,name,marks,city)
 VALUES(1,'arham',93.56,'mumbai'),
 (2,'kanav',94,'pune'),
 (3,'rishaan',87,'delhi');

SELECT *FROM students


create table salesman(
  salesID INt,
  name varchar(255),
  comission decimal(5,2),
  city varchar(255)
 );
 insert into salesman(salesid,name,comission,city)
 VALUES(1,'arham',20000,'mumbai'),
 (2,'kanav',15000,'pune'),
 (3,'rishaan',30000,'delhi');

SELECT *FROM salesman where comission>15000;
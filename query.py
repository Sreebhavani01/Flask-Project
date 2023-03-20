import sqlite3
mydb=sqlite3.connect("query.db")
c=mydb.cursor()
c.execute("create table queries(Name varchar(50), Phone varchar(10), Address varchar(50), Queries varchar(100))")
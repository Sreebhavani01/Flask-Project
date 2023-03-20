import sqlite3
mydb=sqlite3.connect("order.db")
c=mydb.cursor()
c.execute("create table orders(Name varchar(50), Phone varchar(10), Address varchar(50), Email varchar(100), DishName varchar(50), Date varchar(50), Amount varchar(10))")
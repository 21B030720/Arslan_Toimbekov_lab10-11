import psycopg2
from psycopg2 import Error
create_table_query = '''CREATE TABLE mobile
                          (ID INT PRIMARY KEY     NOT NULL,
                          MODEL           TEXT    NOT NULL,
                          PRICE         REAL); '''
create_table_query = '''CREATE TABLE item (
	    item_id serial NOT NULL PRIMARY KEY,
	    item_name VARCHAR (100) NOT NULL,
    	    purchase_time timestamp NOT NULL,
	    price INTEGER NOT NULL
    );'''
connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="Loli0",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")
cursor = connection.cursor()
#cursor.execute("create table ")
def csv(cursor):
    m = []
    with open('addresses.csv', 'r') as f:
        f = f.read()
        f = f.split('\n')
        for i in f:
            m.append(i.split(','))
        print(m)
    k = 1
    m.pop()
    for i in m:
        l = "INSERT INTO mobile (ID, MODEL, PRICE) VALUES ({}, '{}', '{}')".format(k, i[0], i[len(i)-1])
        cursor.execute(l)
        k += 1
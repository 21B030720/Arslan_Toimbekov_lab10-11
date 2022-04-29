from csv_worker import *
from creating import create_data, create_table
# INSERT INTO mobile (ID, MODEL, PRICE) VALUES (1, 'Samsung', 200)
# INSERT INTO mobile (ID, MODEL, PRICE) VALUES (1, 'Samsung', 200)
# select * from mobile
#
#create_data(connection)
#create_table(connection)
while True:
    s = input()
    if s == "csv":
        csv(cursor)
    else:
        try:
            cursor.execute(s)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            connection = psycopg2.connect(user="postgres",
                                          # пароль, который указали при установке PostgreSQL
                                          password="Loli0",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="postgres_db")
            cursor = connection.cursor()
        if 'select' in s:
            try:
                result = cursor.fetchall()
                print(result)
                print()
            except (Exception, Error) as error:
                print("Ошибка при работе с PostgreSQL", error)
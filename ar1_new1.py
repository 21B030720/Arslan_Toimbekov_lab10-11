import psycopg2

host = "127.0.0.1"
user = "postgres"
password = "admin"
db_name = "postgres"

try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )

    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")

    #CREATE
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE IF NOT EXISTS users(
    #             name varchar(50) NOT NULL,
    #             phone_num int NOT NULL);"""
    #     )

    #     print("Table created successfully")
    

    #INSERT
    # with connection.cursor() as cursor:
    #     name1 = input()
    #     phone_num1 = int(input())
    #     cursor.execute(
    #         """INSERT INTO users (name, phone_num) VALUES
    #         ('{}', '{}');""".format(name1, phone_num1)
    #     )

    #     print("Data was successfully inserted")


    #UPDATE NUM
    # with connection.cursor() as cursor:
    #     name2 = input()
    #     update_num = int(input())
    #     cursor.execute(
    #         """UPDATE users SET phone_num = ('{}') WHERE name = ('{}');""".format(update_num, name2)
    #     )

    #     print("Data was successfully updated")


    # #UPDATE NAME
    # with connection.cursor() as cursor:
    #     name2 = input()
    #     update_num = int(input())
    #     cursor.execute(
    #         """UPDATE users SET name = ('{}') WHERE phone_num = ('{}');""".format(name2, update_num)
    #     )

    #     print("Data was successfully updated")

    
    #UPLOAD CSV
    cursor = connection.cursor()
    with open('data.csv', 'r') as f:
        m = []
        f = f.read()
        f = f.split('\n')
        for i in f:
            m.append(i.split(','))
        print(m)
    m.pop()
    for i in m:
        l = "INSERT INTO users (name, phone_num) VALUES ('{}', {})".format(i[0], i[1])
        cursor.execute(l)
    
    print("Data was successfully uploaded")


    #DELETE
    # with connection.cursor() as cursor:
    #     num = int(input())
    #     cursor.execute(
    #         "DELETE FROM users WHERE phone_num = ({});".format(num)
    #     )

    #     print("Data was successfully deleted")



except Exception as ex:
    print("Error while workig with PostgreSQL", ex)

finally:
    if connection:
        connection.close()
        print("PostgreSQL connection closed")

import psycopg2

host = "127.0.0.1"
user = "postgres"
password = "Loli0"
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
    #      cursor.execute(
    #          """CREATE TABLE IF NOT EXISTS snake_player(
    #              name varchar(50) NOT NULL,
    #              level int NOT NULL);"""
    #      )
    #
    #      print("Table created successfully")


    #INSERT
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO users (name, phone_num) VALUES
    #         ('Ramzes', '111');"""
    #     )
    #
    #     print("Data was successfully inserted")


    #DELETE
    # with connection.cursor() as cursor:
    #     num = int(input())
    #     cursor.execute(
    #         "DELETE FROM users WHERE phone_num = ({});".format(num)
    #     )

    #     print("Data was successfully deleted")



except Exception as ex:
    print("Error while workig with PostgreSQL")

finally:
    if connection:
        connection.close()
        print("PostgreSQL connection closed")

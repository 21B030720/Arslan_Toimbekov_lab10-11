import psycopg2
def insert(id, name, ):

    host = "127.0.0.1"
    user = "postgres"
    password = "Loli0"
    db_name = "postgres"

    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT version();"
            )
        # # CREATE
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """CREATE TABLE IF NOT EXISTS snake_player(
        #             id INT PRIMARY KEY     NOT NULL,
        #             name varchar(50) NOT NULL,
        #             level int NOT NULL);"""
        #     )

            print("Table created successfully")
        #INSERT
        print(f"Server version: {cursor.fetchone()}")
        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO snake_player (name, phone_num) VALUES
                ('Ramzes', '111');"""
            )

            print("Data was successfully inserted")
    except Exception as ex:
        print("Error while workig with PostgreSQL", ex)
    finally:
        if connection:
            connection.close()
            print("PostgreSQL connection closed")
insert()
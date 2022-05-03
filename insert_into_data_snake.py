import psycopg2
import pygame
def data_insert(name, level):
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
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         "SELECT version();"
        #     )
        # print(f"Server version: {cursor.fetchone()}")
        # # CREATE
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """CREATE TABLE IF NOT EXISTS snake_player(
        #             id INT PRIMARY KEY     NOT NULL,
        #             name varchar(50) NOT NULL,
        #             level int NOT NULL);"""
        #     )
        # print("Table created successfully")
        #CREATE1
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """CREATE TABLE IF NOT EXISTS snake_rank(
        #             name VARCHAR(20) PRIMARY KEY     NOT NULL,
        #             level int NOT NULL);"""
        #     )
        #     print("Table created successfully")
        #INSERT
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO snake_rank (name, level) VALUES ('{}', {}) ON CONFLICT DO NOTHING;".format(name, level)
            )
            cursor.execute(
                "select * from snake_rank where name='{}'".format(name)
            )
            data = list(cursor.fetchone())
            #print(int(data[1]))
            if level > int(data[1]):
                cursor.execute(
                    "update snake_rank set level={} where name='{}';".format(level, name)
                )
                #print("0000000000000000")
            #print("Data was successfully inserted")
    except Exception as ex:
        print("Error while workig with PostgreSQL", ex)
    finally:
        if connection:
            connection.close()
            #print("PostgreSQL connection closed")
def data_get():
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
                "select * from snake_rank order by -level;"
            )
            data = cursor.fetchall()
            print(data)

    except Exception as ex:
        print("Error while workig with PostgreSQL", ex)
    finally:
        if connection:
            connection.close()
            #print("PostgreSQL connection closed")
def data_show(screen, x, y):
    font = pygame.font.SysFont('comicans', 30, True, False)
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
                "select * from snake_rank order by -level;"
            )
            data = cursor.fetchall()
            k = 0
            for i in data:
                screen.blit(font.render(f'{i[0]}    {i[1]}', True, ((0,0,0))), (x, y + 25 * k))
                #screen.blit(font.render(f'Level:{Score // 5}', True, WHITE), (410, 210))
                k += 1

    except Exception as ex:
        print("Error while workig with PostgreSQL", ex)
    finally:
        if connection:
            connection.close()
#data_get()
#data_insert('Arslan', 200)
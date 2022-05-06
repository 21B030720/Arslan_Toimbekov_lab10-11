import psycopg2
def data_delete(searching):
    searching = str(searching)
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
            cursor.execute("delete from telephone where name = '{}' on conflict do nothing".format(searching))
            if searching.isdigit():
                cursor.execute("delete from telephone where number = {} on conflict do nothing".format(searching))
                cursor.execute("delete from telephone1 where number = {} on conflict do nothing".format(searching))
            cursor.execute("delete from telephone1 where name = '{}' on conflict do nothing".format(searching))

    except Exception as ex:
        print("Error while workig with PostgreSQL", ex)
    finally:
        if connection:
            connection.close()
            print("PostgreSQL connection closed")
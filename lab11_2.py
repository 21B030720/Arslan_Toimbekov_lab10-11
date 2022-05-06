import psycopg2
def data_create_or_update(name, surname, telephone):
    #searching = str(searching)
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
            cursor.execute("select * from telephone where name = '{}' and surname = '{}'".format(name, surname))
            m = cursor.fetchall()
            if list(m) == []:
                print("ok")
                cursor.execute("insert into telephone(name, surname, number) values ('{}', '{}', {}) on conflict do nothing;".format(name, surname, str(telephone)))
            cursor.execute("update telephone set number = {} where name = '{}' and surname = '{}';".format(str(telephone), name, surname))

    except Exception as ex:
        print("Error while workig with PostgreSQL", ex)
    finally:
        if connection:
            connection.close()
            print("PostgreSQL connection closed")

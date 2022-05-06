import psycopg2
def data_get(searching):
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
            cursor.execute(
                "select * from telephone"
            )
            result = list(cursor.fetchall())
            for i in result:
                truth = False
                for j in i:
                    if searching in str(j):
                        truth = True
                if truth:
                    print("Name: {}    Surname: {}    Telephone number: {}".format(str(i[0]), str(i[1]), str(i[2])))
            #print(result)

    except Exception as ex:
        print("Error while workig with PostgreSQL", ex)
    finally:
        if connection:
            connection.close()
            print("PostgreSQL connection closed")
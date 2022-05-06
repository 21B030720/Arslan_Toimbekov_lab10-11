import psycopg2
def data_4(num):
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
                "select * from telephone order by number;"
            )
            result = list(cursor.fetchall())
            k = 0
            for i in result:
                print(" {}   Name: {}   Surname: {}   Telephone: {}".format(str(k+1), i[0], i[1], str(i[2])))
                k +=1
                if k == num:
                    break

    except Exception as ex:
        print("Error while workig with PostgreSQL", ex)
    finally:
        if connection:
            connection.close()
            print("PostgreSQL connection closed")
import psycopg2
def data_3(file):
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
            m = []
            with open(file, 'r') as f:
                f = f.read()
                f = f.split('\n')
                for i in f:
                    m.append(i.split(','))
                m.pop()
                #print(m)

            for i in m:
                # i[0] = i[0].replace(" ", '')
                # i[1] = i[1].replace(" ", '')
                # i[2] = i[2].replace(" ", '')
                if int(i[2]) // 80000000000 == 1:
                    print("Good")
                    l = "INSERT INTO telephone1 (name, surname, number) VALUES ('{}', '{}', '{}') on conflict do nothing;".format(str(i[0]), str(i[1]), str(i[2]))
                    try:
                        cursor.execute(l)
                    except Exception as ex:
                        print(ex, i)
                else:
                    print("Name: {}   Surname: {}   Telephone: {}". format(i[0], i[1], i[2]))

    except Exception as ex:
        print("Error while workig with PostgreSQL", ex)
    finally:
        if connection:
            connection.close()
            print("PostgreSQL connection closed")
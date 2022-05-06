#searching = str(searching)
import psycopg2
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
        cursor.execute("""CREATE TABLE telephone1(
                 name varchar(50) NOT NULL,
                 surname varchar(50) NOT NULL,
                 number varchar(50) PRIMARY KEY NOT NULL);""")
        print("Succesfully")
        cursor.execute("select * from telephone")
        result = cursor.fetchall()
        print(result, "Good")
except Exception as ex:
    print("Error while workig with PostgreSQL", ex)
finally:
    if connection:
        connection.close()
        print("PostgreSQL connection closed")

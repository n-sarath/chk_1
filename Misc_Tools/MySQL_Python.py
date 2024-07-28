import mysql.connector
# As per saved PDF document example..


def create_new_database():
    db_connection = mysql.connector.connect(
        host= "localhost",
        user= "root",
        passwd= "!ongestPassword"
    )
    # creating database_cursor to perform SQL operation
    db_cursor = db_connection.cursor()
    # executing cursor with execute method and pass SQL query
    db_cursor.execute("CREATE DATABASE ipam_database")
    # get list of all databases
    db_cursor.execute("SHOW DATABASES")
    # print all databases
    for db in db_cursor:
        print(db)


def delete_existing_database():
    db_connection = mysql.connector.connect(
        host= "localhost",
        user= "root",
        passwd= "!ongestPassword"
    )
    # creating database_cursor to perform SQL operation
    db_cursor = db_connection.cursor()
    # executing cursor with execute method and pass SQL query
    db_cursor.execute("DROP DATABASE my_first_db")
    # get list of all databases
    db_cursor.execute("SHOW DATABASES")
    # print all databases
    for db in db_cursor:
        print(db)


def connect_to_db():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="!ongestPassword",
        database="ipam_database"
    )

    db_cursor = db_connection.cursor()

    return db_connection, db_cursor


def disconnect_from_db(db_connection, db_cursor):
    # Close the cursor and connection
    db_cursor.close()
    db_connection.close()


def create_table():
    db_connection, db_cursor = connect_to_db()

    db_cursor.execute("CREATE TABLE ipam_db_table (host_name VARCHAR(10) PRIMARY KEY,           \
                        user_name VARCHAR(10), password VARCHAR(10), mgmt_ip VARCHAR(15),       \
                        GigabitEthernet1_ip VARCHAR(15), GigabitEthernet1_mask VARCHAR(15),     \
                        GigabitEthernet2_ip VARCHAR(15), GigabitEthernet2_mask VARCHAR(15),     \
                        GigabitEthernet4_ip VARCHAR(15), GigabitEthernet4_mask VARCHAR(15))")

    db_cursor.execute("SHOW TABLES")
    for table in db_cursor:
        print(table)

    disconnect_from_db(db_connection, db_cursor)


def show_all_tables():

    db_connection, db_cursor = connect_to_db()

    db_cursor.execute("SHOW TABLES")
    for table in db_cursor:
        print(table)

    disconnect_from_db(db_connection, db_cursor)


def drop_table():
    db_connection, db_cursor = connect_to_db()

    # Here creating database table as employee with primary key
    db_cursor.execute("DROP TABLE employee")

    # Here creating database table as student'
    db_cursor.execute("SHOW TABLES")
    for table in db_cursor:
        print(table)

    disconnect_from_db(db_connection, db_cursor)


def drop_all_tables():
    db_connection, db_cursor = connect_to_db()

    # Get the list of all tables
    db_cursor.execute("SHOW TABLES")

    tables = db_cursor.fetchall()

    # Loop through all tables and drop each one
    for table in tables:
        table_name = table[0]
        drop_table_query = "DROP TABLE {0}".format(table_name)
        db_cursor.execute(drop_table_query)

    print("All tables dropped successfully.")


    # Here creating database table as student'
    db_cursor.execute("SHOW TABLES")
    for table in db_cursor:
        print(table)

    disconnect_from_db(db_connection, db_cursor)


def insert_record_table():
    db_connection, db_cursor = connect_to_db()

    employee_sql_query_1 = "INSERT INTO ipam_db_table (host_name, user_name, password, mgmt_ip)  \
                            VALUES ('R1', 'sarath', 'cisco', '192.168.215.140')"

    # Execute cursor and pass query of employee and data of employee
    db_cursor.execute(employee_sql_query_1)
    # db_cursor.execute(employee_sql_query_2)

    db_connection.commit()
    print(db_cursor.rowcount, "Record Inserted")

    disconnect_from_db(db_connection, db_cursor)


def update_record_table():
    db_connection, db_cursor = connect_to_db()

    # Execute the SQL query
    # new = 'newPW'
    # db_cursor.execute(f"UPDATE ipam_db_table SET password = '{new}' WHERE host_name = 'R1'")

    db_cursor.execute(f"UPDATE ipam_db_table SET GigabitEthernet1_ip = '192.168.215.140' WHERE host_name = 'R1'")
    db_cursor.execute(f"UPDATE ipam_db_table SET GigabitEthernet1_mask = '255.255.255.0' WHERE host_name = 'R1'")

    db_cursor.execute(f"UPDATE ipam_db_table SET GigabitEthernet2_ip = '15.1.0.1' WHERE host_name = 'R1'")
    db_cursor.execute(f"UPDATE ipam_db_table SET GigabitEthernet2_mask = '255.255.255.0' WHERE host_name = 'R1'")

    db_cursor.execute(f"UPDATE ipam_db_table SET GigabitEthernet4_ip = '19.1.0.1' WHERE host_name = 'R1'")
    db_cursor.execute(f"UPDATE ipam_db_table SET GigabitEthernet4_mask = '255.255.255.0' WHERE host_name = 'R1'")


    # Commit the transaction
    db_connection.commit()


def insert_record_table_2():
    db_connection, db_cursor = connect_to_db()

    employee_sql_query_1 = "INSERT INTO ipam_db_table (host_name, user_name, password, mgmt_ip)  \
                            VALUES ('R2', 'sarath', 'cisco', '192.168.215.138')"

    # Execute cursor and pass query of employee and data of employee
    db_cursor.execute(employee_sql_query_1)
    # db_cursor.execute(employee_sql_query_2)

    db_connection.commit()
    print(db_cursor.rowcount, "Record Inserted")

    disconnect_from_db(db_connection, db_cursor)


def update_record_table_2():
    db_connection, db_cursor = connect_to_db()

    # Execute the SQL query
    # new = 'newPW'
    # db_cursor.execute(f"UPDATE ipam_db_table SET password = '{new}' WHERE host_name = 'R1'")

    db_cursor.execute(f"UPDATE ipam_db_table SET GigabitEthernet1_ip = '192.168.215.138' WHERE host_name = 'R2'")
    db_cursor.execute(f"UPDATE ipam_db_table SET GigabitEthernet1_mask = '255.255.255.0' WHERE host_name = 'R2'")

    db_cursor.execute(f"UPDATE ipam_db_table SET GigabitEthernet2_ip = '15.1.0.2' WHERE host_name = 'R2'")
    db_cursor.execute(f"UPDATE ipam_db_table SET GigabitEthernet2_mask = '255.255.255.0' WHERE host_name = 'R2'")

    db_cursor.execute(f"UPDATE ipam_db_table SET GigabitEthernet4_ip = '19.1.0.2' WHERE host_name = 'R2'")
    db_cursor.execute(f"UPDATE ipam_db_table SET GigabitEthernet4_mask = '255.255.255.0' WHERE host_name = 'R2'")


    # Commit the transaction
    db_connection.commit()


def delete_record_table():
    db_connection, db_cursor = connect_to_db()

    # Define the ID of the record you want to delete
    hostname_to_delete = 'R1'

    # Execute the SQL query
    db_cursor.execute(f"DELETE FROM ipam_db_table WHERE host_name = 'R1'")

    # Commit the transaction
    db_connection.commit()


def fetch_all_data_db_table():
    db_connection, db_cursor = connect_to_db()

    # Execute a query
    db_cursor.execute("SELECT * FROM ipam_db_table")

    # Fetch all the rows
    rows = db_cursor.fetchall()

    for row in rows:
        print(row)

    disconnect_from_db(db_connection, db_cursor)


def fetch_one_data_db_table():
    db_connection, db_cursor = connect_to_db()

    # Execute a query
    # db_cursor.execute("SELECT * FROM employee")
    db_cursor.execute("SELECT GigabitEthernet4_ip FROM ipam_db_table WHERE host_name = 'R1'")
    data_1 = db_cursor.fetchone()
    # print(data)

    # just process as a Tuple
    print(data_1[0])

    db_cursor.execute("SELECT user_name FROM ipam_db_table WHERE host_name = 'R1'")
    data_3 = db_cursor.fetchone()
    print(data_3[0])

    db_cursor.execute("SELECT password FROM ipam_db_table WHERE host_name = 'R1'")
    data_4 = db_cursor.fetchone()
    print(data_4[0])

    db_cursor.execute("SELECT mgmt_ip FROM ipam_db_table WHERE host_name = 'R1'")
    data_5 = db_cursor.fetchone()
    print(data_5[0])


    disconnect_from_db(db_connection, db_cursor)


if __name__ == '__main__':

    # create_new_database()
    # # delete_existing_database()

    # create_table()
    # # drop_table()
    # # drop_all_tables()

    # insert_record_table()
    # update_record_table()
    # insert_record_table_2()
    # update_record_table_2()
    # # delete_record_table()

    # fetch_all_data_db_table()
    # # fetch_one_data_db_table()

    # # show_all_tables()

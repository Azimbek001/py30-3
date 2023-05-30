import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = False
    try:
        conn = sqlite3.connect(db_file)
    except Error:
        print(Error)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error:
        print(Error)


def create_student(conn, student):
    sql = '''INSERT INTO student(full_name,mark,hobby,b_date)
     VALUES (?,?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error:
        print(Error)


def reed(conn):
    try:
        sql = '''SELECT * FROM student'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for i in rows:
            print(i)
    except Error:
        print(Error)


def update_student_fullname(conn, id, full_name):
    sql = "UPDATE student SET full_name=? WHERE id=?"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (full_name,id))
        conn.commit()
    except Error:
        print(Error)


database = r'group_30.db'

sql_create_table = '''
CREATE TABLE student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR (50) NOT NULL,
mark DOUBLE (5,2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
b_date DATE NOT NULL
);
'''

connection = create_connection(database)

if connection is not None:
    print('все работает')
    # create_table(connection, sql_create_table)
    # create_student(connection, ('beka', 4, None, '2003-06-06'))
    update_student_fullname(connection,2,'sultan')
    reed(connection)
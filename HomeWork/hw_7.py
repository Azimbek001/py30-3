import sqlite3

def create_students_table():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                    (id INTEGER PRIMARY KEY,
                    hobby TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    birth_year INTEGER,
                    homework_score INTEGER)''')
    conn.commit()
    conn.close()

def insert_students_data():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    students_data = [
        ('Reading', 'Ruslan', 'Rizaev', 1998, 8),
        ('Painting', 'Azim', 'Mustapaev', 1999, 12),
        ('Singing', 'Akmal', 'Atakanov', 1997, 15),
        ('Sports', 'Sanjar', 'Konushbekov', 1998, 6),
        ('Gaming', 'Akdil', 'Keneshbekov', 1999, 14),
        ('Cooking', 'Salamat', 'Biygaziev', 1997, 10),
        ('Photography', 'Imaraliev', 'Omurbek', 1998, 9),
        ('Writing', 'Usupbekov', 'Beksultan', 1999, 11),
        ('Music', 'Kazybekov', 'Bakay', 1997, 13),
        ('Dancing', 'Usubaliev', 'Adil', 1998, 7)
    ]
    cursor.executemany('INSERT INTO students (hobby, first_name, last_name, birth_year, homework_score) VALUES (?, ?, ?, ?, ?)', students_data)
    conn.commit()
    conn.close()

def delete_students_with_even_id():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id % 2 = 0")
    conn.commit()
    conn.close()

def update_students_names_to_genius():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET first_name = 'genius' WHERE homework_score > 10")
    conn.commit()
    conn.close()

def get_students_with_long_last_names():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE length(last_name) > 10')
    results = cursor.fetchall()
    conn.close()
    return results

def get_students_with_genius_names():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE first_name = 'genius'")
    results = cursor.fetchall()
    conn.close()
    return results

create_students_table()

insert_students_data()

long_last_names_students = get_students_with_long_last_names()
print("Студенты с фамилией более 10 символов:")
for row in long_last_names_students:
    print(row)

update_students_names_to_genius()

genius_students = get_students_with_genius_names()
print("Студенты с именем 'genius':")
for row in genius_students:
    print(row)

delete_students_with_even_id()

updated_long_last_names_students = get_students_with_long_last_names()
print("Студенты с фамилией более 10 символов (после удаления):")
for row in updated_long_last_names_students:
    print(row)

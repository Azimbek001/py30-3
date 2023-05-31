import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students
                (id INTEGER PRIMARY KEY,
                hobby TEXT,
                first_name TEXT,
                last_name TEXT,
                birth_year INTEGER,
                homework_score INTEGER)''')

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

cursor.execute('SELECT * FROM students WHERE length(last_name) > 10')
results = cursor.fetchall()
print("Студенты с фамилией более 10 символов:")
for row in results:
    print(row)

cursor.execute("UPDATE students SET first_name = 'genius' WHERE homework_score > 10")

cursor.execute("SELECT * FROM students WHERE first_name = 'genius'")
results = cursor.fetchall()
print("Студенты с именем 'genius':")
for row in results:
    print(row)

cursor.execute("DELETE FROM students WHERE id % 2 = 0")

conn.commit()

conn.close()
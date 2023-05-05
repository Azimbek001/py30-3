with open('results.txt', 'r', encoding="UTF-8") as file:
    data = file.readlines()

students = {}
for line in data:
    name_marks = line.strip().split()
    name, grade = name_marks[0], name_marks[2]
    students[name] = {'grade': int(grade)}

sorted_students = dict(sorted(students.items(), key=lambda x: x[1]['grade'], reverse=True))

for student in list(sorted_students)[:3]:
    print(student, sorted_students[student])

with open("sorted_results.txt", "w") as file:
    for name, grade in sorted_students.items():
        file.write(f"{name} {grade}\n")
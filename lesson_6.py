
#функции, аргументы *args, **kwargs
# DRY - don't repeat yourself
# def - definite (определить)
"""function scheme
# определение наименование(параметры):
#     тело функции
#     возвращение результата
#
# наименование(аргументы) # вызов функции
"""

# students = ['Azimbek', 'Ruslan', 'Klim', 'Janargul']
#
#
# def find_student(name: str) -> bool:
#     """
#     Функция принимает имя в виде строки,
#     возвращает булевое значение.
#     """
#     if name.title() in students:
#         return True
#     else:
#         return False
#
#
# def add(name):
#     if find_student(name):
#         print(f'student {name} already exists')
#     else:
#         students.append(name)
#
#
# while True:
#     print(students)
#     commands = input('1) add\n'
#                      '0) exit\n')
#     if commands == '1':
#         add(name=input('input name: ').title())
#     elif commands == '0':
#         print('exit...')
#         break



# print(sum.__doc__)
# print(find_student.__doc__)

# print(help(len))
# print(help(find_student))







# def func(a, *c, b=0, **d):
#     print(f'a - {a}, b - {b}, c - {c}, d - {d}')
#     return (a, b ,c, d)
#
#
# print(func(2, 7, 3, 4, 5, o=9, g=6))



# def menu(**kwargs):
#     return kwargs
#
#
# monday = menu(drink='cola', eat='pizza', dessert='cake')
# print(monday)


# def plus(*args):
#      return sum(args)
#
#
#  print(plus(2, 3, 7, 1.3, 67, 212, 45.9, 279.7))





# print(len('123') + 7)
# print(sum([1, 2, 3]))

# def len1(sequence):
#     counter = 0
#     for _ in sequence:
#         counter += 1
#     return counter
#
#
# print(len1('') + 7)


# def greet(name, age=18):  # name - positional required parameter
#     print(f'name: {name.title()} age: {age}')
#
#
# greet('Janargul', 19)
# greet('Klim')  # Klim - required positional argument
# greet('Ruslan')
# greet(age=17, name='azimbek')  # keyword arguments


# def get_square(width, length):
#     return width * length
#
#
# square_1 = get_square(6, 7)
# square_hall = get_square(10, 24)
# print(square_1, square_hall, sep='\n')

# width = 6
# length = 7
# square_1 = width * length
# print(square_1)
#
# width = 10
# length = 24
# square_hall = width * length
# print(square_hall)
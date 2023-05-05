day1 = float(input("Введите расход за понедельник: "))
day2 = float(input("Введите расход за вторник:  "))
day3 = float(input("Введите расход за среду:  "))
day4 = float(input("Введите расход за четверг: "))
day5 = float(input("Введите расход за пятницу: "))
day6 = float(input("Введите расход за субботу: "))
day7 = float(input("Введите расход за воскресенье: "))

total_expenses = day1 + day2 + day3 + day4 + day5 + day6 + day7
average_expenses=total_expenses / 7
print("Общие расходы за неделю:",round(total_expenses,1) )
print("Средние расходы в день:",round(average_expenses,1))

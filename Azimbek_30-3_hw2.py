# Запрос у пользователя дня и месяца рождения
day = int(input("Введите день рождения (число от 1 до 31): "))
month = int(input("Введите месяц рождения (число от 1 до 12): "))
#проверка
if (day < 1 or day > 31) or (month < 1 or month > 12):
    print("Неправильный ввод. Введите корректные значения дня и месяца рождения.")
else:
    # Определение знака зодиака по дню и месяцу рождения
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        zodiac = "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <=20):
        zodiac = "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        zodiac = "Близнецы"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        zodiac = "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac = "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        zodiac = "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
        zodiac = "Весы"
    elif (month == 10 and day >= 24) or (month == 11 and day <= 21):
        zodiac = "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        zodiac = "Стрелец"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        zodiac = "Козерог"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        zodiac = "Водолей"
    else:
        zodiac = "Рыбы"

    print("Ваш знак зодиака:"+ zodiac)

    rounds = 5
    while True:
        if rounds == 0:
            break
        print(rounds)
        rounds -= 1
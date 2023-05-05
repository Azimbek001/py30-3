vowels = "aeiouаеёиоуыэюя"
consonants = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ"
while True :
    vowels2 = 0
    consonants2 = 0
    word = input("Введите слово на (рус,анг):exit что бы завершить:").lower()
    if word == "exit" or word == "выход":
        print("Программа завершена")
        break
    letters = len(word)
    for i in word:
        if i in vowels:
            vowels2 += 1
        elif i in consonants:
            consonants2 += 1

    print(f"Слово: {word}")
    print(f"Количество букв: {letters}")
    print(f"Гласные буквы: {vowels2}")
    print(f"Согласные буквы: {consonants2}")
    print(f'Гласные/Согласные: {round(vowels2 / len(word) * 100, 2)}%'""f': {round(consonants2 / len(word) * 100, 2)}%')
mentors = ["Кубаныч", "Мирлан", "Гулина", "Камиля"]

while True:
    print("Выберите действие:")
    print("1) Добавление")
    print("2) Изменение")
    print("3) Удаление")
    print("0) Выход")
    choice = input()

    if choice == "1":
        if len(mentors) >= 10:
            print("В списке уже есть 10 менторов, добавление невозможно.")
        else:
            name = input("Введите имя ментора: ")
            if len(name) > 15:
                print("Имя не должно содержать более 15 букв.")
            elif name.title() in mentors:
                print("Такой ментор уже есть в списке.")
            else:
                name = name.title()
                mentors.append(name)
                print("Ментор успешно добавлен.")

    elif choice == "2":
        old_name = input("Введите имя заменяемого ментора: ")
        if old_name.title() not in mentors:
            print("Такого ментора нет в списке.")
        else:
            new_name = input("Введите новое имя ментора: ")
            if len(new_name) > 15:
                print("Имя не должно содержать более 15 букв.")
            elif new_name.title() in mentors and new_name.title() != old_name.title():
                print("Такой ментор уже есть в списке.")
            else:
                index = mentors.index(old_name.title())
                mentors[index] = new_name.title()
                print("Ментор успешно изменен.")

    elif choice == "3":
        print("Выберите способ удаления:")
        print("1) По имени")
        print("2) По индексу")
        del_choice = input()

        if del_choice == "1":
            name = input("Введите имя ментора: ")
            if name.title() not in mentors:
                print("Такого ментора нет в списке.")
            else:
                mentors.remove(name.title())
                print("Ментор успешно удален.")
        elif del_choice == "2":
            index = input("Введите индекс ментора: ")
            if not index.isdigit() or int(index) >= len(mentors):
                print("Некорректный индекс.")
            else:
                del mentors[int(index)]
                print("Ментор успешно удален.")
        else:
            print("Некорректный выбор.")

    elif choice == "0":
        break

    else:
        print("Некорректный выбор.")

mentors_tuple = tuple(mentors)
print("Список менторов:", mentors_tuple)

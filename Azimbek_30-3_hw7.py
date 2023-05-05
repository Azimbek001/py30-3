
ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0, ten))
squared_evens = list(map(lambda x: x ** 2, evens))

print(squared_evens)

def print_item_by_index(lst=ten):
    if lst is None:
        lst = list(range(1, 11))

    while True:
        try:
            index = input("Введите индекс элемента (или введите 'exit' для выхода): ")

            if index.lower() == 'exit':
                print("Выход из программы.")
                break

            index = int(index)
            print(f"Элемент с индексом {index}: {lst[index]}")
        except IndexError:
            print(f"Неверный индекс! Введите число от 0 до {len(lst) - 1}")
        except ValueError:
            print("Некорректный ввод! Введите целое число или 'exit' для выхода.")

print_item_by_index()


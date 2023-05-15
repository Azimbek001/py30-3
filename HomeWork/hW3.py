class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму для внесения на счет: "))
        self._balance += amount
        print(f"Ваш новый баланс: {self._balance}")

    def _kill(self):
        self._balance = 0
        print(f"Ваш баланс обнулен: {self._balance}")

    def __jackpot(self):
        self._balance *= 10
        print(f"Ваш баланс увеличен в 10 раз: {self._balance}")

    def merge_balance(self, other):
        self._balance += other._balance
        print(f"Ваш обновленный баланс после объединения: {self._balance}")

person1 = Bank("Person1", 100)
person2 = Bank("Person2", 200)

person1.moneyX()
person1._kill()
person1.merge_balance(person2)

print(f"Баланс Person1: {person1._balance}")
print(f"Баланс Person2: {person2._balance}")







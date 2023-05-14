#2 Задание Calculator
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a

    def __sub__(self, other):
        return self.a - other.a

    def __mul__(self, other):
        return self.a * other.a

    def __truediv__(self, other):
        if other.a != 0:
            return self.a / other.a
        else:
            return "Деление на ноль невозможно!"

calc1 = Calculator(10, 2)
calc2 = Calculator(5, 3)

result_add = calc1 + calc2
result_sub = calc1 - calc2
result_mul = calc1 * calc2
result_div = calc1 / calc2

print(f"Результат сложения: {result_add}")
print(f"Результат вычитания: {result_sub}")
print(f"Результат умножения: {result_mul}")
print(f"Результат деления: {result_div}")



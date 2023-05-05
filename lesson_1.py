def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '**':
        return num1 ** num2
    elif operator == '%':
        return num1 % num2
    else:
        return "Invalid operator"

result = calculator(2, '**', 3)
print(result)

result = calculator(5, '+', 9.6)
print(result)

result = calculator(20, '%', 3)
print(result)

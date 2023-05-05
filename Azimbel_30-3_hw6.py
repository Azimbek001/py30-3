#1
def multiply_numbers(*args):
    result = 1
    for number in args:
        result *= number
    return result

print(multiply_numbers(2, 3, 4, 5))

#2
def is_palindrome(i='hello'):
    return i == i[::-1]

print(is_palindrome('abccba'))  # True
print(is_palindrome('hello'))   # False

#3
def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    elif operator == '**':
        return num1 ** num2
    else:
        return "Invalid operator"

print(calculator(2, '**', 3))  # 8
print(calculator(5, '+', 9.6)) # 14.6
print(calculator(20, '%', 3))  # 2

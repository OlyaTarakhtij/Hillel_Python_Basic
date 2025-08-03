a = float(input('Введить перше число: '))
operation = input('Введіть математичну операцію (+, -, *, /): ')
b = float(input('Введіть друге число:'))
if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    if b != 0:
        result = a / b
    else:
        b = float(input('Помилка: ділення на нуль! Введіть друге число, більше за 0: '))
        result = a / b
print("Результат: ", result)
while True:
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
            b = float(input('Помилка: ділення на нуль! Введіть друге число, яке не дорівнює 0: '))
            result = a / b
    else:
        print('Невідома операція!') # Перевірка, якщо користувач введе некоректну операцію
        continue

    print("Результат: ", result)

#Умова для продовження обчислень
    choice = input('Бажаєте продовжити обчислення? y/n: ').lower() # переводить введені користувачем літери у нижній регістр
    if choice != 'y':
        print('Завершення обчислень. ')
        break
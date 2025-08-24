import math

number = int(input('Введіть будь-яке число: '))
if int(number) > 9:
    while number > 9:
        list_number = [int(ch) for ch in str(number)]  # отримуємо список із цифр
        number = math.prod(list_number) #перемножуємо елементи списку
    print('Результат множення: ', number)
else:
    print("Результат множення дорівнює введеному числу: ", number)
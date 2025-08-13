import random
random_list = [random.randint(0, 100) for i in range(random.randint(3, 10))]
print('Список з випадкової довжини від 3 до 10 елемнетів:', random_list)
new_list = [random_list[0], random_list[2], random_list[-2]]
print('Новий список з трьох елементів: ', new_list)
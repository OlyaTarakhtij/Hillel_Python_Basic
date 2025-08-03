n = int(input('Введить 4-значне число: '))
n_1 = n // 1000
n_2 = (n % 1000) // 100
n_3 = (n % 100) // 10
n_4 = n % 10
print(n_1)
print(n_2)
print(n_3)
print(n_4)
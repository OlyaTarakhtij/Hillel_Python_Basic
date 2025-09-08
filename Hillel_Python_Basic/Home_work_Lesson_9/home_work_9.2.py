def difference(*args):
    if not args:   # якщо аргументів немає
        return 0
    return round(max(args) - min(args), 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -0.5) == 5.5, 'Test2'
assert difference() == 0, 'Test3'
assert difference(10.2, 5.567, 8.3) == 4.63, 'Test4'

print("ОК")

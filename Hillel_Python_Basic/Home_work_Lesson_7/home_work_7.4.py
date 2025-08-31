def common_elements():
    list_mult_3 = {x for x in range(100) if x % 3 == 0}
    list_mult_5 = {x for x in range(100) if x % 5 == 0}
    return list_mult_3 & list_mult_5

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('OK')

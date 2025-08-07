my_list = [0, 1, 0, 12, 3]
list_zeros = my_list.count(0)
none_zeros = [x for x in my_list if x != 0]
new_list = none_zeros + [0] * list_zeros
print(new_list)
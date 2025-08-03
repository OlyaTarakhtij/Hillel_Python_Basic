my_list = [25, 4, 19, 82, 28, 8, 20, 12]
lengh_my_list = len(my_list)
if lengh_my_list % 2 == 0:
    half_list = len(my_list) // 2
    first_half = my_list[:half_list]
    second_half = my_list[half_list:]
    result_list = [first_half, second_half]
    print(result_list)
else: lengh_my_list % 2 != 0
half_list = len(my_list) // 2 + 1
first_half = my_list[:half_list]
second_half = my_list[half_list:]
result_list = [first_half, second_half]
print(result_list)
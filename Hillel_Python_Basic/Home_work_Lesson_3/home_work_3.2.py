new_list = [7, 82, 25, 19, 54, 108]
if len(new_list) < 2:
    print(new_list)
else:
    new_list = [new_list[-1]] + new_list[:-1]
    print(new_list)
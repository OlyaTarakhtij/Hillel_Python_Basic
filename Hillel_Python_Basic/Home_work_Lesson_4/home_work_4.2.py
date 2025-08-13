list_int = [0, 1, 7, 2, 4, 8]
if not list_int:
    print(0)
else:
    even_list = list_int[::2]
    result = sum(even_list) * list_int[-1]
    print(result)
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list[2] = 100
modified_tuple = tuple(my_list)
print(modified_tuple)
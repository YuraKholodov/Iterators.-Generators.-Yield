
list_of_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


flat_list = [j for i in list_of_list for j in i]
print(flat_list)
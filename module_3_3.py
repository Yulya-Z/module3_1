def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)
values_list_ = (5, 'ball', False)
values_dict_ = {'a': 1, 'b': 'string', 'c': True}
values_list_2 = (54.32, 'String')

print_params(*values_list_)
print_params(**values_dict_)
print_params(*values_list_2, 42)
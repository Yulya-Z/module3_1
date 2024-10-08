data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    sum_num = 0
    sum_strings = 0

    def recurse(params):
        nonlocal sum_num, sum_strings
        if isinstance(params, list) or isinstance(params, tuple) or isinstance(params, set):
            for i in params:
                recurse(i)
        elif isinstance(params, dict):
            for value in params.values():
                recurse(value)
            for key in params.keys():
                recurse(key)
        elif isinstance(params, int) or isinstance(params, str):
            if isinstance(params, int):
                sum_num += params
            elif isinstance(params, str):
                sum_strings += len(params)

    recurse(data_structure)
    return sum_num + sum_strings

result = calculate_structure_sum(data_structure)
print(result)

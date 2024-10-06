data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(params):
    summa = 0
    for i in params:
        if isinstance(i, int):
            summa += i
        elif isinstance(i, str):
            summa += len(i)
        elif isinstance(i, dict):
            summa += sum(dict.values(i))
        else:
            summa += calculate_structure_sum(i)

    return summa

result = calculate_structure_sum(data_structure)
print(result)
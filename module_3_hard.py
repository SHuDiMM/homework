def calculate_sum(data):
    total = 0

    if isinstance(data, int):
        return data
    elif isinstance(data, str):
        return len(data)
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            total += calculate_sum(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            total += calculate_sum(key)
            total += calculate_sum(value)

    return total


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_sum(data_structure))

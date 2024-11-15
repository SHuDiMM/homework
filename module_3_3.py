def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params('Свекла')
print_params(55, ['a', 'b', 'c'])
print_params(c=False, b=(44, 'Fire', [1, 2, 3]))
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [True, 108, 'Такая сточка']
values_dict = {'a': 'Зеленый', 'b': 444, 'c': 4.45}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Ночь', False]
print_params(*values_list_2, 42)

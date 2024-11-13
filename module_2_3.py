my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_of_element = int(0)
print('Исходные данные:')
print('my_list =', my_list, '''
''')
print('Вывод на консоль:')
while len(my_list) > (index_of_element + 1):
    if my_list[index_of_element] > 0:
        print(my_list[index_of_element])
        index_of_element = index_of_element + 1
    elif my_list[index_of_element] < 0:
        break
    else:
        index_of_element = index_of_element + 1
        continue

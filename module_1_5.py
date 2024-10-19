# immutable_var = (10, 105.28, "The Lord Of The Rings")
# print(immutable_var)
# immutable_var[0] = 11 #TypeError: 'tuple' object does not support item assignment - кортежи не поддерживают назначение(изменение) элементов внутри себя.
# immutable_var[1] = immutable_var[1]*2 #TypeError: 'tuple' object does not support item assignment - кортежи не поддерживают назначение(изменение) элементов внутри себя.
# immutable_var[2] = immutable_var[2] + ' is a great book' #TypeError: 'tuple' object does not support item assignment - кортежи не поддерживают назначение(изменение) элементов внутри себя.
# print(immutable_var)

mutable_list = ["Stalker", 25.17, 42]
mutable_list[0]= mutable_list[0]+' - old game'
mutable_list[1]= mutable_list[1]-3
mutable_list[2]= mutable_list[2]/12
print(mutable_list)
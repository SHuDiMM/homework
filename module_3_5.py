def get_multiplied_digits(number=int()):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

result_1 = get_multiplied_digits(40203)
print(result_1)
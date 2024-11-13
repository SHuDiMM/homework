answers = []
n = int(input('Введите число n (3-20): n = '))
for i in range(1, 20):
    for j in range(i+1, 20):
        is_true = n % (i+j) == 0
        if is_true == True and i != j:
            answers.extend([i, j])
            continue
        else:
            continue
print('Пароли: ', *answers)
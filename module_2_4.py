numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(0, len(numbers) + 1):
    if i == 1 or i == 0:
        continue
    elif i == 2:
        primes.append(i)
        continue
    else:
       is_prime = True
       for j in range(2, i):
            is_prime = i % j != 0
            if is_prime == True:
                continue
            else:
                break
       if is_prime == True:
           primes.append(i)
       else:
           not_primes.append(i)
print ('''Исходный код:
numbers=''', numbers)
print('Вывод на консоль:')
print("Primes:",primes)
print("Not Primes:",not_primes)

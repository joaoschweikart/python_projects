def contador(*num):
    total = 0
    for n in num:
        total = total + n
    print(f'Recebi os valores {num} e a soma deles é igual a {total}.')


contador(0, 9, 4, 2, 10)

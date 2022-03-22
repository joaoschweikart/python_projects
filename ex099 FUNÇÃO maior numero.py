maiornum = 0
from time import sleep


def maior(*num):
    maiornum = 0
    for c in range(0, len(num)):
        if num[c] > maiornum:
            maiornum = num[c]
    print('-='*25)
    print('ANALISANDO OS VALORES PASSADOS....')
    sleep(1)
    for n in num:
        print(n, end=' ')
        sleep(0.5)
    if len(num) == 0:
        print('Não foi informado nenhum valor.')
    else:
        print(f'foi fo(ram) o(s) valor(es) informado(s), sendo {len(num)} número(s) ao todo.')
    sleep(1)
    print(f'O maior valor informado foi o número {maiornum}.')
    sleep(1)


maior(2, 9, 4, 5, 13, 9, 3)

maior(4, 7, 0)

maior(6)

maior()

maior(321, 3213214, 32, 3232)

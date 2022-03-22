print('=-' *20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-' *20)

from random import randint
from time import sleep
c = 0

while True:
    num = int(input('Digite um número: '))
    pi = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    computador = randint(0, 10)
    soma = num + computador
    print('PROCESSANDO...')
    sleep(1)
    if pi not in 'PIÍ':
        pi = str(input('Código inválido. Digite novamente [P/I]: '))
    if soma % 2 == 0:
        print(f'Você jogou {num} e o computador jogou {computador}. O total é {soma}, portanto, é PAR!')
        if pi == 'P':
            print('=-' * 20)
            print('Você venceu! Vamos jogar novamente!')
            print('=-' * 20)
            c = c + 1
        else:
            print('=-' * 20)
            print('Você perdeu! GAMEOVER!')
            break
    if soma % 2 == 1:
        print(f'Você jogou {num} e o computador jogou {computador}. O total é {soma}, portanto, é ÍMPAR!')
        if pi in 'IÍ':
            print('=-' * 20)
            print('Você venceu! Vamos jogar novamente!')
            print('=-' * 20)
            c = c + 1
        else:
            print('=-' * 20)
            print('Você perdeu! GAMEOVER!')
            break

sleep(1)
print('=-' *20)
print(f'Você conseguiu {c} vitória(s) consecutiva(s)!')
print('=-' *20)










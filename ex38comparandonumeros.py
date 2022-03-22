import time
print('COMPARANDO DOIS NÚMEROS')
print('=-'*30)
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro: '))
print('=-'*30)
print('PROCESSANDO...')
time.sleep(2)
if n1 > n2:
    print('O \033[7:40mprimeiro valor\033[m ({}) é maior que o segundo valor ({}).'.format(n1, n2))
elif n2 > n1:
    print('O \033[7:40msegundo valor\033[m ({}) é maior que o primeiro valor ({}).'.format(n2, n1))
else:
    print('Os dois valores são iguais!')



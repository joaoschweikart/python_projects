print('=-'*20)
print('CÁLCULO DE FATORIAL')
print('=-'*20)
from math import factorial

n = int(input('Digite um número inteiro para descobrir seu fatorial: '))
f = factorial(n)
c = n
print('Calculando fatorial de {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c = c - 1
print('{}'.format(f))
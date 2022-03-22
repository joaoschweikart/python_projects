print('=-'*30)
print('DESCUBRA SE O NÚMERO QUE VOCÊ ESTÁ PENSANDO É PRIMO OU NÃO!')
print('=-'*30)
n = int(input('Digite um número inteiro: '))
cont = 0
#FAZENDO COM if

#if n == 2 or n == 3 or n == 5:
    #print('O número {} É PRIMO!'.format(n))
#elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n == 1:
    #print('O número {} NÃO É PRIMO!'.format(n))
#else:
    #print('O número {} É PRIMO!'.format(n))

#FAZENDO COM for

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' '.strip())
        cont = cont + 1
    else:
        print('\033[31m', end=' '.strip())
    print('{}'.format(c),end=' ')

if cont == 2:
    print('\n\033[mO número {} foi divisível {} vezes, portanto, ele é primo.'.format(n, cont))
else:
    print('\n\033[mO número {} foi divisível {} vezes, portanto, ele não é primo.'.format(n, cont))


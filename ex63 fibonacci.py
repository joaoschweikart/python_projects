print('=-'*25)
print('SEQUÊNCIA DE FIBONACCI')
print('=-'*25)

n = int(input('Digite quantos valores você quer visualizar da \033[33mSequência de Fibonacci\033[m: '))
cont = 3
t1 = 0
t2 = 1
print('{} > {} > '.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print('{} > '.format(t3), end='')
    cont = cont + 1
    t1 = t2
    t2 = t3

print('FIM!')

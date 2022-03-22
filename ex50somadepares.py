print('=-'*30)
print('DIGITE 6 NÚMEROS INTEIROS:')
print('=-'*30)
soma = 0
for c in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma = soma + n
print('A soma dos números pares que você escreveu é igual a {}'.format(soma))

print('=-'*50)
print('-----------\033[33mLEITOR DE NÚMEROS INTEIROS:\033[m------------')
print('O PROGRAMA VAI SOMAR TODOS OS NÚMEROS DIGITADOS E SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999.')
print('=-'*50)
n = 0
soma = 0
cont = -1
while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input('Digite um número inteiro qualquer para somar ou o número 999 para interromper o programa: '))
print('Foram digitados {} números ao total.'.format(cont))
print('A soma total entre os números digitados é igual a {}!'.format(soma))



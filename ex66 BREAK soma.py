print('=-'*50)
print('\033[33mLEITOR DE NÚMEROS INTEIROS:\033[m')
print('O PROGRAMA VAI SOMAR TODOS OS NÚMEROS DIGITADOS E SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999.')
print('=-'*50)
soma = 0
cont = 0
while True:
    n = int(input('Digite um número inteiro qualquer para somar ou o \033[33mnúmero 999 para interromper o programa:\033[m '))
    if n == 999:
        break
    soma = soma + n
    cont = cont + 1

print(f'Foram digitados {cont} números ao total, e a soma de todos eles é igual a {soma}!')


print('=-'*50)
print('-----------\033[33mLEITOR DE NÚMEROS INTEIROS:\033[m------------')
print('O PROGRAMA VAI MOSTRAR A MÉDIA ENTRE OS NÚMEROS DIGITADOS E SÓ VAI PARAR QUANDO O USUÁRIO QUEIRA.')
print('=-'*50)
from time import sleep

cont = 0
n = 0
soma = 0
maior = 0
menor = 0
iniciar = 'S'

while iniciar == 'S':
    n = int(input('Digite um número inteiro: '))
    cont = cont + 1
    soma = soma + n
    if cont == 1:
        maior = menor = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    sleep(0.5)
    iniciar = str(input('Deseja inserir mais valores? \033[33m[SIM/NÃO]\033[m: ')).strip().upper()[0]

print('A média entre todos os números digitados foi igual a {}, \nsendo o maior número = {} e o menor número = {}.'.format(soma/cont, maior, menor))



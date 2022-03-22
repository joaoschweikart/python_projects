print('=-'*30)
print('\033[33mMENU DE ESCOLHAS (SOMA, MULTIPLICAÇÃO e MAIOR VALOR)\033[m')
print('=-'*30)
from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

opcao = 0
while opcao == 1 or 2 or 3 or 4 or 5:
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MOSTRAR O MAIOR VALOR
[4] DIGITAR NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    opcao = int(input('Digite a opção que você deseja realizar: '))
    if opcao == 1:
        print('PROCESSANDO...')
        sleep(1)
        print('A soma dos números {} e {} é igual a {}.'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('PROCESSANDO...')
        sleep(1)
        print('A multiplicação dos números {} e {} é igual a {}.'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('PROCESSANDO...')
            sleep(1)
            print('O maior valor entre os números {} e {} é o {}.'.format(n1, n2, n1))
        if n2 > n1:
            print('PROCESSANDO...')
            sleep(1)
            print('O maior valor entre os números {} e {} é o {}.'.format(n1, n2, n2))
        if n1 == n2:
            print('PROCESSANDO...')
            sleep(1)
            print('Os números são iguais!')
    elif opcao == 4:
        print('PROCESSANDO...')
        sleep(1)
        n1 = int(input('Digite um novo valor: '))
        n2 = int(input('Digite outro novo valor: '))
        print('''[1] SOMAR
[2] MULTIPLICAR
[3] MOSTRAR O MAIOR VALOR
[4] DIGITAR NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    elif opcao == 5:
        print('FINALIZANDO...')
        sleep(2)
        print('Fim do programa.')
        exit()
    elif opcao >= 6:
        print('Código inválido. Tente novamente!')
    sleep(2)

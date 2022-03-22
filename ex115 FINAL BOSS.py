from ex115 import *
from time import sleep
arq = 'lista.txt'


while True:
    escreva('MENU PRINCIPAL')
    escreva('1 - VER PESSOAS CADASTRADAS\n'
            '2 - CADASTRAR NOVAS PESSOAS\n'
            '3 - SAIR DO SISTEMA')
    while True:
        linha()
        opcao = leiaint('\033[34mDigite sua opção: \033[m')
        if opcao == 1:
            #opção 1: mostra a lista de pessoas já cadastradas no lista.txt através de uma def 'lerarquivo'
            escreva('PESSOAS CADASTRADAS')
            lerarquivo(arq)
            sleep(2)
            break
        elif opcao == 2:
            #opção 2: cadastra novas pessoas na lista.txt através de uma def 'adicionarnoarquivo'
            escreva('NOVO CADASTRO')
            adicionarnoarquivo(arq)
            print('\033[4;32mPessoa cadastrada com sucesso!!! :D\033[m')
            sleep(2)
            break
        elif opcao == 3:
            #opção 3: finaliza o programa
            escreva('FINALIZANDO PROGRAMA...')
            sleep(1)
            exit()
        else:
            #opção x: nenhuma das opções anteriores, obriga o usuário a digitar uma opção válida
            print('\033[31mERRO! Digite uma opção válida!\033[m')
            sleep(1.5)


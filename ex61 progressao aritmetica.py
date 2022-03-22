print('=-' * 30)
print('PROGRESSÃO ARITMÉTICA')
print('=-' * 30)
pt = int(input('Digite o primeiro termo de uma progressão: '))
razao = int(input('Digite a razão dessa progressão: '))
termo = pt #faz com que o primeiro termo sirva de base para a progressão
cont = 1 #serve para que o contador vá até 10 itens

while cont < 11:
    print('{} >'.format(termo), end=' ')
    termo = termo + razao #constrói os próximos ites da progressão (termo + razão = 8 + 3 = 11 + 3 = 14 + 3 = 17.....)
    cont = cont + 1 #serve para aumentar um nível do contador até chegar a 10
print('FIM!', end='')

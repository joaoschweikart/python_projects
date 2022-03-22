pt = int(input('Digite o primeiro termo de uma progressão: '))
razao = int(input('Digite a razão dessa progressão: '))
termo = pt #termo iniciador que dará sequencia aos próximos
cont = 1 #contador de termos da progressão
repeticoes = 10 #quantas vezes a progressão vai se repetir na primeira vez
total = 0 #total de termos a ser mostrados
while repeticoes != 0:
    total = total + repeticoes
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA!')
    repeticoes = int(input('Digite quantos termos mais você quer descobrir: '))
print('FIM!')





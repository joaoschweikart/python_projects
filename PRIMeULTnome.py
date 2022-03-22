#LER O NOME COMPLETO DE UMA PESSOA MOSTRANDO EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE
nome = str(input('Digite seu nome: ')).strip().split()
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu segundo nome é {}.'.format(nome[len(nome)-1]))



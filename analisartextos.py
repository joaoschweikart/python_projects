nome = input(str('Digite seu nome: ')).strip()
print('Nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Total de letras sem considerar os espaços: {}'.format(len(nome) - nome.count(' ')))
print('Total de letras no primeiro nome: {}'.format(nome.find(' ')))








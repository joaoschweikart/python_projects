print('ANO BISSEXTO')
ano = int(input('Digite um ano qualquer: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} se trata de um ano bissexto.'.format(ano))
else:
    print('O ano {} não é um ano bissexto.'.format(ano))




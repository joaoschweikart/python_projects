produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90, "Camisa do Grêmio", 250.00)
print('='*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('='*50)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>6.2f}')








#print(produtos[0].ljust(40, '.'), end='')
#print('R$ ', end='')
#print('{:.2f}'.rjust(8).format(produtos[1]))
#print(produtos[2].ljust(40, '.'), end='')
#print('R$ ', end='')
#print('{:.2f}'.rjust(8).format(produtos[3]))
#print(produtos[4].ljust(40, '.'), end='')
#print('R$ ', end='')
#print('{:.2f}'.rjust(8).format(produtos[5]))
#print(produtos[6].ljust(40, '.'), end='')
#print('R$ ', end='')
#print('{:.2f}'.rjust(8).format(produtos[7]))
#print(produtos[8].ljust(40, '.'), end='')
#print('R$ ', end='')
#print('{:.2f}'.rjust(8).format(produtos[9]))
#print(produtos[10].ljust(40, '.'), end='')
#print('R$ ', end='')
#print('{:.2f}'.rjust(8).format(produtos[11]))
#print(produtos[12].ljust(40, '.'), end='')
#print('R$ ', end='')
#print('{:.2f}'.rjust(8).format(produtos[13]))
#print(produtos[14].ljust(40, '.'), end='')
#print('R$ ', end='')
#print('{:.2f}'.rjust(8).format(produtos[15]))
#print(produtos[16].ljust(40, '.'), end='')
#print('R$ ', end='')
#print('{:.2f}'.rjust(8).format(produtos[17]))

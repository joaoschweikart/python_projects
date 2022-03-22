print('=-'*24)
print('ENTREVISTANDO 5 PESSOAS PARA DESCOBRIR SEU PESO')
print('=-'*24)

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Qual o peso em kilos da {}ª pessoa?: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MENOR peso lido é {}kg e o MAIOR peso lido é {}kg.'.format(menor, maior))



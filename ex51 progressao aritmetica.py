print('=-' * 30)
print('PROGRESSÃO ARITMÉTICA')
print('=-' * 30)
pt = int(input('Digite o primeiro termo de uma progressão: '))
razao = int(input('Digite a razão dessa progressão: '))
itens = int(input('Digite quantos itens você quer ter em sua P.A: '))
décimo = pt + (itens-1) * razao

for c in range(pt, décimo, razao):
    print('{} '.format(c), end='> ')
print('ESSA É A SUA PROGRESSÃO ARITMÉTICA :)')

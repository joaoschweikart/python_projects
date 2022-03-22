print('=-'*20)
print('CAIXA DE LOJA')
print('=-'*20)

total = 0
p = 0 #produtos mais caros que R$1000
c = 0 #contador de itens
precomaisbarato = 0
nomemaisbarato = ' '

while True:
    nome = str(input('Qual o nome do produto?: '))
    preco = float(input('Qual o preço do produto?: R$'))
    total = total + preco
    c = c + 1
    if c == 1:
        precomaisbarato = preco
        nomemaisbarato = nome
    else:
        if preco < precomaisbarato:
            precomaisbarato = preco
            nomemaisbarato = nome
    if preco >= 1000:
        p = p + 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

dinheiro = int(input(f'Quanto você vai dar em dinheiro? (preço total: {total}): '))
print(f'O total gasto na sua compra foi de \033[33mR${total}\033[m.')
print(f'Ao total, \033[33m{p}\033[m produto(s) custou(ram) mais de R$1000.00.')
print(f'O produto mais barato foi \033[33m{nomemaisbarato}\033[m, que custa \033[33mR${precomaisbarato}\033[m.')
print(f'O troco para R${dinheiro:.2f} é de R${dinheiro - total:.2f}')

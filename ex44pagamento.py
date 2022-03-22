print('MÉTODO DE PAGAMENTO')

preço = float(input('Qual o preço da compra?: R$'))
print('''ESCOLHA UM MÉTODO DE PAGAMENTO:
[ 1 ] à vista em dinheiro/cheque (10% de desconto)
[ 2 ] à vista no cartão (5% de desconto)
[ 3 ] 2x no cartão (preço normal)
[ 4 ] 3x ou mais no cartão (20% de juros)''')
pagamento = int(input('Selecione uma opção: '))

if pagamento == 1:
    print('O preço final será de R${} reais'.format(preço - (preço * 10/100)))
elif pagamento == 2:
    print('O preço final será de R${} reais'.format(preço - (preço * 5/100)))
elif pagamento == 3:
    print('O preço final será de R${} reais'.format(preço))
elif pagamento == 4:
    parcelas = int(input('Em quantas parcelas? '))
    print('O preço final será de R${} reais divididos em {} parcelas de R${} reais cada.'.format(preço + (preço * 20/100), parcelas, (preço + (preço * 20/100)) / parcelas))
else:
    print('Método de pagamento inválido. Tente novamente!')



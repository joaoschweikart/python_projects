valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos você vai financiar? '))
prestacaomensal = valor / (anos*12)
if prestacaomensal > salario * 30/100:
    print('Percemos que o valor da prestação mensal (R${:.2f}) é maior que 30% do seu salário mensal, portanto, o seu empréstimo foi negado!'.format(prestacaomensal))
else:
    print('Muito bem, seu empréstimo foi aprovado! A prestação mensal de pagamento da casa será de R${:.2f}'.format(prestacaomensal))
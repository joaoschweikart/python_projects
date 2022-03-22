print('AUMENTO DE SALÁRIO em 15% ou 10%')
salario = float(input('Qual é o seu salário?: R$'))
if salario > 1250.0:
    print('Com um aumento de 10%, seu novo salário é de R${:.2f} reais'.format(salario*10/100+salario))
else:
    print('Com um aumento de 15%, seu novo salário é de R${:.2f} reais'.format(salario*15/100+salario))

import time
print('PAR OU ÍMPAR')
print('=-' *20)
num = float(input('Digite um número qualquer: '))
resto = num % 2
print('PROCESSANDO....')
time.sleep(2)
print('=-'*20)
if resto == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é ímpar!'.format(num))

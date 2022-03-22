from time import sleep
print('=-'*30)
print('Vamos calcular sua média!')
print('=-'*30)
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
média = (nota1 + nota2) / 2
print('PROCESSANDO...')
sleep(2)
if média < 5.0:
    print('Sua média é de {:.2f}. Você está reprovado!'.format(média))
elif média >= 7.0:
    print('Sua média é de {:.2f}! Você foi aprovado sem recuperação!'.format(média))
else:
    print('Sua média é de {:.2f}! Você está de recuperação!'.format(média))




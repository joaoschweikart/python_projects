import time

print('=-' * 40)
print('LIMITE DE VELOCIDADE')
print('=-' * 40)
velocidade = float(input('Há quantos km/h seu carro está andando nessa rodovia?: '))
print('=-' * 40)
print('PROCESSANDO...')
time.sleep(2)
if velocidade > 80:
    print('Você está andando acima do limite de velocidade de 80km/h.')
    print('A multa custa R$7 por cada km acima do limite!')
    print('CALCULANDO SUA MULTA...')
    time.sleep(2)
    multa = (velocidade - 80) * 7
    print('Sua multa será de R${} reais'.format(multa))
else:
    print('Muito bem! Você está dentro do limite de velocidade de 80km/h!')

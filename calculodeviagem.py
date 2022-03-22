import time
print('PREÇO DA PASSAGEM DE UMA VIAGEM')
print('=-'*30)
print('Em viagens menores que 200km, a passagem custará R$0,50 centavos para cada km rodado.')
print('Em viagens maiores que 200km, a passagem custará R$0,45 centavos para cada km rodado.')
print('=-'*30)
distancia = float(input('Qual será a distância de sua viagem? '))
print('=-' *30)
print('PROCESSANDO...')
time.sleep(2)
if distancia < 200:
    print('Percebemos que o caminho de sua viagem é menor que 200km.')
    print('Portanto, cada km percorrido custará R$0,50 centavos.')
    print('O preço de sua viagem será de R${} reais.'.format(distancia*0.5))
else:
    print('Percebemos que o caminho de sua viagem é maior que 200km.')
    print('Portanto, cada km percorrido custará R$0,45 centavos.')
    print('O preço de sua viagem será de R${} reais.'.format(distancia*0.45))

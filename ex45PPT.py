from random import randint
from time import sleep

sorteio = randint(1, 3)

print('===PEDRA, PAPEL E TESOURA===')

print('''Vamos jogar! Escolha entre pedra, papel e tesoura:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
a = int(input('Digite o número correspondente a sua escolha: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)

if sorteio == 1 and a == 1:
    print('O computador escolheu a opção PEDRA! Nós empatamos :0')
elif sorteio == 1 and a == 2:
    print('O computador escolheu a opção PEDRA! Você venceu :(')
elif sorteio == 1 and a == 3:
    print('O computador escolheu a opção PEDRA! Você perdeu :D')
elif sorteio == 2 and a == 1:
    print('O computador escolheu a opção PAPEL! Você perdeu :D')
elif sorteio == 2 and a == 2:
    print('O computador escolheu a opção PAPEL! Nós empatamos :0')
elif sorteio == 2 and a == 3:
    print('O computador escolheu a opção PAPEL! Você venceu :(')
elif sorteio == 3 and a == 1:
    print('O computador escolheu a opção TESOURA! Você venceu :(')
elif sorteio == 3 and a == 2:
    print('O computador escolheu a opção TESOURA! Você perdeu :D')
elif sorteio == 3 and a == 3:
    print('O computador escolheu a opção TESOURA! Nós empatamos :0')
else:
    print('Número inválido. Tente colocar números correspondestes as opções (1, 2 ou 3)!')

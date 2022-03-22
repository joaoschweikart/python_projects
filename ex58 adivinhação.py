from random import randint

sorteado = randint(0, 10)
tentativas = 1

print('=-' * 20)
print('---------JOGO DA ADIVINHAÇÃO----------')
print('=-' * 20)

n = int(input('Estou pensando em um número inteiro entre 0 e 10. Adivinhe qual é: '))
while sorteado != n:
    n = int(input('EERRRROUUUU!!! Tente novamente um número entre 0 e 10: '))
    tentativas = tentativas + 1

print('Eu escolhi o número {}.'.format(sorteado))
print('Você acertou! Parabéns!')
print('Você precisou de {} tentativas para acertar o número escolhido.'.format(tentativas))

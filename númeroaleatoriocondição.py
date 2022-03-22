import random
import time
sorteado = random.randint(0, 5)
print('JOGO DA ADIVINHAÇÃO')
print('=-' * 40)
n = int(input('Estou pensando em um número inteiro de 0 a 5. Adivinhe qual é: '))
print('=-' * 40)
print('PROCESSANDO...')
time.sleep (2) #efeito de (processamento)
print('Eu escolhi o número {}'.format(sorteado))
if n == sorteado:
    print('Você acertou! Parabéns!')
else:
    print('ERRRRRROUUUUUU! Mais sorte na próxima vez :D')






from time import sleep
from random import randint
from operator import itemgetter

jogadores = {}
print('=-'*25)
for c in range(1, 5):
    n = randint(0, 6)
    print(f'O JOGADOR-{c} tirou o número {n}')
    jogadores[f'JOGADOR-{c}'] = n
    sleep(1)

print('=-'*25)
print('RANKING DOS JOGADORES:')
print('=-'*25)

c = 1
for k, v in sorted(jogadores.items(), key=itemgetter(1), reverse=True):
    sleep(1)
    print(f'{c}º lugar: {k} que tirou {v}.')
    c = c+1


print('=-'*25)
print('MEGA SENA')
print('=-'*25)
jogos = int(input('Quantos jogos você quer que eu sorteie?: '))
megasena = []
from time import sleep
from random import randint

print(f'========== SORTEANDO {jogos} JOGOS ==============')
sleep(0.5)

for a in range(0, jogos):
    for c in range(0, 6):
        n = randint(1, 60)
        if n not in megasena:
            megasena.append(n)
        else:
            megasena.append(n+1)
    print(f'Jogo {a+1}: {sorted(megasena)}')
    megasena.clear()
    sleep(0.5)
print('=-'*25)
print('BOA SORTE!')

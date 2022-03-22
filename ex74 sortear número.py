from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os números sorteados foram {n}.')

print('=-'*23)
print(f'O MAIOR valor sorteado foi o {max(n)}.')
print(f'O MENOR valor sorteado foi o {min(n)}.')
print('=-'*23)

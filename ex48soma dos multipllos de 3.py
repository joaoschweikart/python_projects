print('=-'*30)
print('SOMA DOS MÚLTIPLOS DE 3 ÍMPARES do número 1 ao 500!')
print('=-'*30)
soma = 0
for n in range(3, 501, 3):
    if n % 2 == 1:
        soma = soma + n
print('A soma de todos os números múltiplos de 3 ímpares entre 1 e 500 é ígual à {}!'.format(soma))




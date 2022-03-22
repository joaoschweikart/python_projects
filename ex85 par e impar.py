lista = [[], []]

for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

print('=-'*30)
print(f'Lista completa: {lista}')
print('=-'*30)
print(f'Valores pares em ordem crescente: {sorted(lista[0])}.')
print('=-'*30)
print(f'Valores ímpares em ordem crescente: {sorted(lista[1])}.')
print('=-'*30)

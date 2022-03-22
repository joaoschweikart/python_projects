lista = []
pares = []
impares = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continuar = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar not in 'SN':
        continuar = str(input('Código inválido. Você quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

print('=-'*20)
print('Essas são suas listas:')
print(f'Lista completa: {lista}')
print('=-'*20)
print(f'Lista de números pares: {pares}')
print('=-'*20)
print(f'Lista de números ímpares: {impares}')
print('=-'*20)

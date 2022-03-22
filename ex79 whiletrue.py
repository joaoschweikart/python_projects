valores = []

while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor computado com sucesso.')
    else:
        print('Valor já digitado anteriormente.')
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Código inválido. Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Esses são os valores que você digitou em ordem crescente: {sorted(valores)}')


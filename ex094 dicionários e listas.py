pessoa = {}
galera = []
mulheres = []
cont = 0 #número de pessoas cadastradas
total = 0 #soma da idade das pessoas
maiores = []

while True:
    pessoa['Nome'] = str(input('Digite seu nome: ')).upper().strip()
    pessoa['Sexo'] = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'])
    pessoa['Idade'] = int(input('Digite sua idade: '))
    total += pessoa['Idade']
    galera.append(pessoa.copy())
    cont += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if continuar == 'N':
        break

media = total / cont
for p in galera:
    if p['Idade'] > media:
        maiores.append(p['Nome'])

print('=-'*30)
print(galera)
print('=-'*30)

print(f'Ao total, foram cadastradas {cont} pessoas.')
print(f'A média de idade do grupo foi {media:.2f} anos.')
print(f'As mulheres cadastradas foram as seguintes: {mulheres}')
print(f'As pessoas que estão acima da média de idade de {media:.2f} anos são as seguintes: {maiores}')

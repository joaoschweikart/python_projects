lista = []

while True:
    n = int(input('Digite um número para colocar na lista: '))
    lista.append(n)
    continuar = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar not in 'SN':
        continuar = str(input('Código inválido. Você quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

print('=-'*30)
print(f'A sua lista de números é essa: {lista}')
print('=-'*30)
print('Ao todo, foram digitados {} números.'.format(len(lista)))
print('=-'*30)
lista.sort(reverse=True)
print(f'A lista ordenada de forma DECRESCENTE é: {lista}')
print('=-'*30)
if 5 in lista:
    print(f'O valor 5 está na lista e aparece pela primeira vez na posição {lista.index(5)+1}.')
else:
    print('O valor 5 não está na lista.')
print('=-'*30)

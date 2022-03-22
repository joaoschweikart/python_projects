tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))

print('=-'*25)
print(f'Você digitou os valores {tupla}.')
print('=-'*25)
print(f'O número 9 apareceu {tupla.count(9)} vez(es).')
print('=-'*25)
if 3 in tupla:
    print(f'O número 3 foi digitado pela primeira vez na {tupla.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print('=-'*25)
print(f'Os números pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')

valores = []
posicaomaior = []
posicaomenor = []

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for p, v in enumerate(valores):
    if v == max(valores):
        posicaomaior.append(p+1)
    if v == min(valores):
        posicaomenor.append(p+1)

print('=-'*25)
print(f'Sua lista: {valores}')
print('=-'*25)
print(f'O maior valor digitado na lista foi o NÚMERO {max(valores)} na(s) posição(ões) {posicaomaior}')
print(f'O menor valor digitado na lista foi o NÚMERO {min(valores)} na(s) posição(ões) {posicaomenor}')
print('=-'*25)

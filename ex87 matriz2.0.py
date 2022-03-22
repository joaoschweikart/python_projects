matriz = [[], [], []]
parescont = 0
terceiracont = 0
maiorsegunda = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para a posição [{l + 1}, {c + 1}] da matriz: ')))
        if matriz[l][c] % 2 == 0:
            parescont = parescont + matriz[l][c]
        if c == 2:
            terceiracont = terceiracont + matriz[l][c]
        if l == 1:
            if c == 0:
                maiorsegunda = matriz[l][c]
            else:
                if matriz[l][c] > maiorsegunda:
                    maiorsegunda = matriz[l][c]

print('=-' * 30)
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{matriz[c][d]:^5}]', end='')
    print()
print('=-' * 30)
print(f'A soma dos valores PARES é igual a {parescont}.')
print(f'A soma dos valores da TERCEIRA COLUNA é igual a {terceiracont}.')
print(f'O maior valor da SEGUNDA LINHA é igual a {maiorsegunda}.')
print('=-' * 30)

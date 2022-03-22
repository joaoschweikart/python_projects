matriz = [[], [], []]

for c in range(0, 3):
    for d in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para a posição [{c+1}, {d+1}] da matriz: ')))

print('=-'*30)
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{matriz[c][d]:^5}]', end='')
    print()

print('=-'*30)


'''print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]'
      f'\n[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]'
      f'\n[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')'''
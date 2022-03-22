print('=-'*30)
print('GOLS EM PARTIDAS DE FUTEBOL')
print('=-'*30)

jogador = {}
gols = []

jogador['Nome'] = str(input('Qual o nome do jogador?: '))
jogador['Número de partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
jogador['Total de gols'] = 0

for c in range(1, jogador['Número de partidas']+1):
    n = (int(input(f'Quantos gols {jogador["Nome"]} fez na {c}º partida? ')))
    gols.append(n)
    jogador['Total de gols'] += n

jogador['Gols'] = gols[:]


print('=-'*30)
print(jogador)
print('=-'*30)

for k, v in jogador.items():
    print(f'A chave \033[33m{k}\033[m tem o valor {v}.')
print('=-'*30)

print(f'O jogador {jogador["Nome"]} jogou {jogador["Número de partidas"]} partidas ao total.')
c = 0
for v in jogador['Gols']:
    c += 1
    print(f'=> Na {c}º partida, o jogador {jogador["Nome"]} fez {v} gols.')
print('=-'*30)
print(f'Total de {jogador["Total de gols"]} gols.')

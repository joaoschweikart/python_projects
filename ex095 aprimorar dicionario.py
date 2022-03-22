jogadores = []
jogador = {}
gols = []

while True:
    jogador['Nome'] = str(input('Qual o nome do jogador?: ')).upper()
    jogador['Número de partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
    jogador['Total de gols'] = 0
    for c in range(1, jogador['Número de partidas']+1):
        n = (int(input(f'Quantos gols {jogador["Nome"]} fez na {c}º partida? ')))
        gols.append(n)
        jogador['Total de gols'] += n
    jogador['Gols'] = gols.copy()
    jogadores.append(jogador.copy())
    gols.clear()
    continuar = str(input('Você deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

print('=-'*25)
print(jogadores)
print('=-'*25)
print('Nº   NOME DO JOGADOR    GOLS              TOTAL DE GOLS')

for k, v in enumerate(jogadores):
    print(f'{k}    {v["Nome"]:<15}    {v["Gols"]}         {v["Total de gols"]}')

print('=-'*10)
print('URNA ELETRÔNICA')
print('=-'*10)
votoslula = 0
votosbolsonaro = 0
votosnulo = 0
while True:
    voto = int(input('DIGITE O NÚMERO DO SEU CANDIDATO: '))
    if voto == 13:
        votoslula += 1
    if voto == 17:
        votosbolsonaro += 1
    if votosbolsonaro % 5 == 0:
        votosbolsonaro -= 1
        votoslula += 1
    if voto != 17 and voto != 13:
        print('SEU VOTO É NULO!')
        votosnulo += 1
    continuar = str(input('DESEJA CONTINUAR? [S/N] ')).strip().upper()
    if continuar != 'N':
        break
print(f'A quantidade de votos para LULA foi {votoslula} e para BOLSONARO foi {votosbolsonaro}, além de'
      f' {votosnulo} votos nulos')


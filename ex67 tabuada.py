print('=-' * 60)
print('TABUADA DE VÁRIOS NÚMEROS')

while True:
    print('=-' * 60)
    n = int(input('Você deseja visualizar a tabuada de qual número? (O programa é interrompido caso um número negativo for digitado): '))
    print('=-' * 60)
    c = 1
    if n < 0:
        print('PROGRAMA ENCERRADO')
        break
    cont = int(input('Quantos valores você deseja ver na sua tabuada?: '))
    while c <= cont:
        print(f'{n} x {c} = {n*c}')
        c = c + 1

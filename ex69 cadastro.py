from time import sleep

a = 0 #total de pessoas com idade maior de 18
b = 0 #total de homens cadastrados
c = 0 #total de mulheres com idade menor de 20

while True:
    print('=-' * 20)
    print('CADASTRE UMA PESSOA')
    print('=-' * 20)
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        a = a + 1
    if sexo == 'M':
        b = b + 1
    if sexo == 'F' and idade <= 20:
        c = c + 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

sleep(1)
print('=-'*20)
print('FIM DO CADASTRO')
print('=-'*20)
print(f'Ao todo, \033[33m{a}\033[m pessoa(s) com 18 anos ou mais foi(ram) cadastrada(s).')
print(f'\033[33m{b}\033[m homem(s) foi(ram) cadastrado(s).')
print(f'\033[33m{c}\033[m mulher(es) com 20 anos ou menos foi(ram) cadastrada(s).')

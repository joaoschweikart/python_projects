print('=-'*25)
print('CAIXA ELETRÔNICO')
print('=-'*25)
from time import sleep

cinquenta = 0
vinte = 0
dez = 0
um = 0

valor = int(input('Qual o valor que você deseja sacar?: R$'))
print('=-'*25)
print(f'O montante de R${valor},00 será dividido em:')
while valor >= 50:
    cinquenta = valor // 50
    valor = valor - cinquenta * 50
    if cinquenta > 0:
        print(f'{cinquenta} cédula(s) no valor de 50 reais;')
while valor >= 20:
    vinte = valor // 20
    valor = valor - vinte * 20
    if vinte > 0:
        print(f'{vinte} cédula(s) no valor de 20 reais;')
while valor >= 10:
    dez = valor // 10
    valor = valor - dez * 10
    if dez > 0:
        print(f'{dez} cédula(s) no valor de 10 reais;')
while valor >= 1:
    um = valor // 1
    valor = valor - um * 1
    if um > 0:
        print(f'{um} cédula(s) no valor de 1 real;')
while valor == 0:
    break

print('=-'*25)


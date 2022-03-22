n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    contador = int(input('Digite um número de 0 a 20: '))

    while contador > 20 or contador < 0:
        contador = int(input('Tente novamente. Digite um número de 0 a 20: '))

    print(f'Você digitou o número {n[contador]}.')

    continuar = str(input('Você deseja continuar e digitar outro número? [S/N]: ')).upper().strip()[0]

    while continuar not in 'SN':
        continuar = str(input('Código inválido. Você deseja continuar e digitar outro número? [S/N]: ')).upper().strip()[0]

    if continuar == 'N':
        break

print('Fim do programa!')
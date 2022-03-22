def leiaint(msg):
    ok = False
    valor = 0
    while True:
        a = str(input(msg))
        if a.isnumeric():
            valor = int(a)
            ok = True
        else:
            print('\033[31mERRO! Digite um número INTEIRO!\033[m')
        if ok:
            break
    return valor


# programa principal
n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}.')

ok = False
while True:
    try:
        a = int(input('Digite um número: '))
        b = int(input('Digite seu divisor: '))
        r = a/b
        ok = True
        if ok:
            break
    except:
        print('Ocorreu um erro no programa. Por favor, tente novamente:')


print(f'A resposta é igual a {r:.2f}')

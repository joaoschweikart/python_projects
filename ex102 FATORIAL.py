from math import factorial


def fatorial(num, show):
    """
    Calcula o fatorial de um número
    :param num: número que será calculado o fatorial
    :param show: opção de mostrar ou não a resolução do fatorial
    :return: valor do fatorial de "num"
    """
    f = factorial(num)
    if show:
        for num in range(num, 0, -1):
            print(f'{num}', end=' x ' if num > 1 else ' = ')
    return f


#programa principal
numero = int(input('Qual número você deseja descobrir o fatorial?: '))
mostrar = int(input('Você deseja mostrar a resolução? [0 para NÃO e 1 para SIM]: '))

if mostrar == 0:
    print(fatorial(numero, show=False))
else:
    print(fatorial(numero, show=True))


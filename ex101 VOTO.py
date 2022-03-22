from datetime import date
atual = date.today().year


def voto(num):
    if 17 < num < 65:
        return 'VOTO OBRIGATÓRIO!'
    elif num < 16:
        return 'SEM PERMISSÃO LEGAL!'
    elif 15 < num < 18 or num > 64:
        return 'VOTO OPCIONAL!'


ano = int(input('Em que ano você nasceu?: '))
idade = atual - ano
print(f'Percemos que você tem {idade} anos, portanto, sua situação de voto é a seguinte: {voto(idade)}')

def ficha(nome, gols):
    """
    escreve o nome do jogador e quantos gols ele marcou
    :param nome: nome do jogador informado
    :param gols: quantidade de gols do jogador
    :return: retorna a frase completa
    """
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome == '':
        nome = 'DESCONHECIDO'
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


#programa principal
jogador = str(input('Qual o nome do jogador?: '))
gol = str(input('Quantos gols ele fez?: '))
print(ficha(jogador, gol))

def notas(*num, sit=False):
    """
    Essa função cria um dicionário que guarda várias informações sobre o boletim de um aluno
    :param num: lista de notas do aluno
    :param sit: situação do aluno (aprovado, reprovado, recuperação)
    :return: retorna o dicionário completo
    """
    boletim = {}
    boletim['Quantidade de notas'] = len(num)
    boletim['Maior'] = max(num)
    boletim['Menor'] = min(num)
    boletim['Média do aluno'] = sum(num) / len(num)
    if sit:
        if boletim['Média do aluno'] >= 7:
            boletim['Situação'] = 'APROVADO'
        elif boletim['Média do aluno'] < 6:
            boletim['Situação'] = 'REPROVADO'
        else:
            boletim['Situação'] = 'RECUPERAÇÃO'
    return boletim


#Programa Principal
resposta = notas(10, 5, 4, 3, 10, 1, 5, sit=True)
print(resposta)

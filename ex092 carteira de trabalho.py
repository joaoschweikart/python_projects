from datetime import date
atual = date.today().year
from time import sleep

cadastro = {}

cadastro['Nome'] = str(input('Qual seu nome?: '))
cadastro['Ano de nascimento'] = int(input('Qual seu ano de nascimento?: '))
cadastro['Carteira de Trabalho'] = int(input('Número da Carteira de Trabalho [não tem = 0]: '))
cadastro['Idade'] = atual - cadastro['Ano de nascimento']
if cadastro['Carteira de Trabalho'] != 0:
    cadastro['Ano de contratação'] = int(input('Qual seu ano de contratação?: '))
    cadastro['Salário'] = float(input('Qual o seu salário?: '))
    cadastro['Ano de aposentadoria'] = cadastro['Ano de contratação'] + 35
    cadastro['Idade de aposentadoria'] = cadastro['Ano de aposentadoria'] - cadastro['Ano de nascimento']
    print('=-' * 30)
    print('Levando em consideração um tempo mínimo de contribuição de 35 anos, os dados são os seguintes:')
    print('=-'*30)
    for k, v in cadastro.items():
        print(f'{k} tem o valor de {v}.')
        sleep(0.6)
else:
    print('=-' * 30)
    for k, v in cadastro.items():
        print(f'{k} tem o valor de {v}.')
        sleep(0.6)

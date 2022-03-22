from time import sleep
from datetime import date
atual = date.today().year
ano = int(input('Qual o seu ano de nascimento?: '))
print('=-'*30)
print('Processando...')
sleep(2)
print('=-'*30)
if atual - ano < 18:
    print('Percebemos que você ainda tem apenas {} anos. Faltam {} anos para o seu alistamento!'.format(atual-ano, ano+18-atual))
elif atual - ano == 18:
    print('Percebemos que você completou/completará 18 anos nesse ano. Aliste-se no site: \033[4malistamento.eb.mil.br\033[m')
else:
    print('Você já tem {} anos. Seu tempo de alistamento já passou! Você deveria ter se alistado em {}!'.format(atual-ano, ano+18))
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

print('=-'*25)
print('ENTREVISTANDO 7 PESSOAS')
print('=-'*25)

for pessoas in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu?: '.format(pessoas)))
    idade = atual - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo, obtivemos {} pessoas MAIORES de idade e {} MENORES de idade!'.format(totmaior, totmenor))


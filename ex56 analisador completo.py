print('=-'*30)
print('ANALISADOR COMPLETO: NOME, IDADE E SEXO DE CADA ENTREVISTADO')
print('=-'*30)

somaidade = 0
media = 0
homemvelho = 0
nomevelho = ''
idademulher = 0

for p in range(1, 5):
    print('---{}ª PESSOA---'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()
    somaidade = somaidade + idade
    media = somaidade / 4

    if p == 1 and sexo == 'M':
        homemvelho = idade
        nomevelho = nome

    if idade > homemvelho and sexo == 'M':
        homemvelho = idade
        nomevelho = nome

    if idade < 20 and sexo == 'F':
        idademulher = idademulher + 1

print('A média de idade final do grupo é de {}!'.format(media))
print('O homem mais velho do grupo é o {}, com {} anos!'.format(nomevelho, homemvelho))
print('Há {} mulher(es) nesse grupo com menos de 20 anos!'.format(idademulher))

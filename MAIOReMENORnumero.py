print('MAIOR E MENOR NÚMERO')
a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
c = int(input('Digite outro: '))
#VERIFICANDO O MENOR NÚMERO:
if a<c and a<b:
    menor = a
if b<c and b<a:
    menor = b
if c<b and c<a:
    menor = c
#VERIFICANDO O MAIOR NÚMERO:
if a > c and a > b:
    maior = a
if b > c and b > a:
    maior = b
if c > b and c > a:
    maior = c
print('O menor número digitado é o {}!'.format(menor))
print('O maior número digitado é o {}!'.format(maior))





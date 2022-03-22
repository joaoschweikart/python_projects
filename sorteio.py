import random
print('===SORTEIO===')
a = input('Digite o nome de um participante: ')
b = input('Outro: ')
c = input('Outro: ')
d = input('Outro: ')
lista = [a, b, c, d]
e = random.choice(lista)
print('O escolhido no sorteio foi o(a) {}.'.format(e))





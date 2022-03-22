from random import shuffle
print('===EMBARALHAR LISTA===')
a = input('Digite um nome: ')
b = input('Outro: ')
c = input('Outro: ')
d = input('Outro: ')
e = input('Outro: ')
f = input('Outro: ')
g = input('Outro: ')
lista = [a, b, c, d, e, f, g]
shuffle(lista)
print('A ordem da lista será:')
print(lista)
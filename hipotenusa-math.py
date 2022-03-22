from math import hypot

print('===HIPOTENUSA c/ MATH====')
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = hypot(co, ca)
print('A hipotenusa desse triângulo retângulo é igual a {:.2f}!'.format(h))


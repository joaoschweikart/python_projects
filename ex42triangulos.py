from time import sleep
print('TRIÂNGULO ESCALENO, ISÓSCELES E EQUILÁTERO:')
r1 = float(input('INSIRA O COMPRIMENTO DE UMA RETA: '))
r2 = float(input('INSIRA O COMPRIMENTO DE UMA OUTRA RETA: '))
r3 = float(input('INSIRA O COMPRIMENTO DE UMA OUTRA RETA: '))
if r1+r2 > r3 and r1+r3 > r2 and r3 + r2 > r1 == r2 == r3:
    print('Essas retas formam um triângulo do tipo Equilátero!')
elif r1+r2 > r3 and r1+r3 > r2 and r3 + r2 > r1 != r2 != r3 != r1:
    print('Essas retas formam um triângulo do tipo Escaleno!')
elif r1+r2 > r3 and r1+r3 > r2 and r3 + r2 > r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
    print('Essas retas formam um triângulo do tipo Isósceles!')
else:
    print('Essas retas não podem formar um triângulo!')

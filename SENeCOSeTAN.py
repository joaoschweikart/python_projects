import math
print('===SENO, COSSENO E TANGENTE===')
a = float(input('Digite o ângulo desejado: '))
co = math.cos(math.radians(a))
se = math.sin(math.radians(a))
tn = math.tan(math.radians(a))
print('O seno, o cosseno e a tangente do ângulo {}º são, respectivamente: {:.2f}, {:.2f} e {:.2f}.'.format(a, se, co, tn))



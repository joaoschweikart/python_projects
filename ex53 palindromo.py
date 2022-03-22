print('=-' * 30)
print('LEITOR DE PALÍNDROMOS')
print('=-' * 30)
frase = str(input('Digite uma frase ou palavra: ').replace(" ", "").upper())
palavras = frase.split()
tudojunto = ''.join(palavras)
inverso = ''
for letra in range(len(tudojunto)-1, -1, -1):
    inverso = inverso + tudojunto[letra]
from time import sleep
print('PROCESSANDO...')
sleep(2)
print('O inverso de {} é igual a {}.'.format(tudojunto, inverso))
if inverso == tudojunto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')

#outra solução:
#frase = str(input('Digite uma frase ou palavra: ').replace(" ", "").upper())
#palavras = frase.split()
#tudojunto = ''.join(palavras)
#inverso = tudojunto[::-1]
#if tudojunto == inverso:
#    print('Temos um palíndromo!')
#else:
#    print('Não temos um palíndromo!')




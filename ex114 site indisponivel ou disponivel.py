from urllib import request

a = 'http://www.pudim.com.br'
try:
    site = request.urlopen(a)
except:
    print(f'\033[31mO site {a} NÃO está disponível no momento.\033[m')
else:
    print(f'\033[32mO site {a} ESTÁ disponível no momento.\033[m')

from time import sleep


def contador(i, f, r):
    if i < f:
        f = f+1
        for c in range(i, f, r):
            print(c, end=' ')
            sleep(0.6)
    elif i > f:
        f = f-1
        if r > 0:
            r = r * -1
            for c in range(i, f, r):
                print(c, end=' ')
                sleep(0.6)
        elif r == 0:
            r = r - 1
            for c in range(i, f, r):
                print(c, end=' ')
                sleep(0.6)
        else:
            for c in range(i, f, r):
                print(c, end=' ')
                sleep(0.6)


print('=-'*20)
print('CONTAGEM DE 1 até 10 DE 1 em 1')
contador(1, 10, 1)
print('FIM!')

print('=-'*20)
print('CONTAGEM DE 10 até 0 DE 2 em 2')
sleep(0.6)
contador(10, 0, -2)
print('FIM!')

print('=-'*20)
print('Agora é sua vez de personalizar a contagem!')
sleep(0.6)
inicio = int(input('INÍCIO: '))
fim = int(input('FIM: '))
razao = int(input('RAZÃO: '))

print('=-'*20)
if razao < 0:
    print(f'CONTAGEM DE {inicio} até {fim} DE {razao*-1} em {razao*-1}:')
elif razao == 0:
    print(f'CONTAGEM DE {inicio} até {fim} DE {razao + 1} em {razao + 1}:')
else:
    print(f'CONTAGEM DE {inicio} até {fim} DE {razao} em {razao}:')
sleep(0.6)
contador(inicio, fim, razao)
print('FIM!')
print('=-'*20)


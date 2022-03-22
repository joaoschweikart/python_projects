lista = []

for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Número adicinado ao fim da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Número adicionado na posição {pos+1}.')
                break
            pos += 1

print(f'A lista dos números digitados, em ordem crescente, é a seguinte: {lista}')

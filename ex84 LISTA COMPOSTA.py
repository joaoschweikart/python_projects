dados = []
listacompleta = []
listamaispesadas = []
listamaisleves = []
contador = 0 #contador de pessoas cadastradas
maiorpeso = 0 #numero do maior peso
menorpeso = 0 #numero do menor peso
nomemaior = '' #nome do mais pesado
nomemenor = '' #nome do menos pesado

while True:
    dados.append(str(input('NOME: ')).upper().strip())
    dados.append(float(input('PESO em KG: ')))
    listacompleta.append(dados[:])
    contador = contador + 1
    if contador == 1:
        menorpeso = listacompleta[0][1]
    dados.clear()
    continuar = str(input('Você deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('=-'*50)
print(f'Foram cadastradas {contador} pessoas ao total.')
print('=-'*50)
for p in listacompleta:
    if p[1] > maiorpeso:
        listamaispesadas.clear()
        maiorpeso = p[1]
        nomemaior = p[0]
        listamaispesadas.append(nomemaior)
    elif p[1] == maiorpeso:
        maiorpeso = p[1]
        nomemaior = p[0]
        listamaispesadas.append(nomemaior)

    if p[1] < menorpeso:
        listamaisleves.clear()
        menorpeso = p[1]
        nomemenor = p[0]
        listamaisleves.append(nomemenor)
    elif p[1] == menorpeso:
        menorpeso = p[1]
        nomemenor = p[0]
        listamaisleves.append(nomemenor)

print(f'A(s) pessoa(s) mais leve(s) é(são): {listamaisleves} com o peso de {menorpeso:.2f}kg.')
print('=-'*50)
print(f'A(s) pessoa(s) mais pesada(s) é(são): {listamaispesadas} com o peso de {maiorpeso:.2f}kg.')
print('=-'*50)

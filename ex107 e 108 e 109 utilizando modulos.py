from ex111.utilidadesCeV import moeda

'''#EX 107
p = float(input('Digite o preço: R$'))
print(f'O dobro do preço de {p} é igual a {numeros.dobro(p)}.')
print(f'A metade do preço de {p} é igual a {numeros.metade(p)}.')
print(f'O preço de {p} com um acréscimo de 10% é igual a {numeros.aumentar10(p)}.')
print(f'O preço de {p} com um desconto de 13% igual a {numeros.diminuir13(p)}.')'''


'''#EX 108
p = float(input('Digite o preço: R$'))
print(f'O dobro do preço de {numeros.moeda(p)} é igual a {numeros.moeda(numeros.dobro(p))}.')
print(f'A metade do preço de {numeros.moeda(p)} é igual a {numeros.moeda(numeros.metade(p))}.')
print(f'O preço de {numeros.moeda(p)} com um acréscimo de 10% é igual a {numeros.moeda(numeros.aumentar10(p))}.')
print(f'O preço de {numeros.moeda(p)} com um desconto de 13% igual a {numeros.moeda(numeros.diminuir13(p))}.')'''


#EX 109
p = float(input('Digite o preço: R$'))
print(f'O dobro do preço de {moeda.moeda(p)} é igual a {moeda.dobro(p, True)}.')
print(f'A metade do preço de {moeda.moeda(p)} é igual a {moeda.metade(p, True)}.')
print(f'O preço de {moeda.moeda(p)} com um acréscimo de 10% é igual a {moeda.aumentar(p, 10, True)}.')
print(f'O preço de {moeda.moeda(p)} com um desconto de 13% igual a {moeda.diminuir(p, 13, True)}.')

def mostrararea(c, l):
    a = c*l
    print(f'A área do terreno com {c}m de comprimento e {l}m de largura é igual a {a:.2f}m².')


print('=-' * 30)
print('TERRENO')
print('=-' * 30)

comprimento = float(input('Digite o COMPRIMENTO do terreno em metros: '))
largura = float(input('Digite a LARGURA do terreno em metros: '))

mostrararea(comprimento, largura)

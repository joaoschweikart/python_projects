print('FORMAR UM TRIÂNGULO COM TRÊS RETAS')
r1 = float(input('INSIRA O COMPRIMENTO DE UMA RETA: '))
r2 = float(input('INSIRA O COMPRIMENTO DE UMA OUTRA RETA: '))
r3 = float(input('INSIRA O COMPRIMENTO DE UMA OUTRA RETA: '))
if r1+r2 > r3 and r1+r3 > r2 and r3+r2 > r1:
    print('Essas retas TÊM a capacidade de formar um triângulo!')
else:
    print('Essas retas NÃO TÊM a capacidade de formar um triângulo')

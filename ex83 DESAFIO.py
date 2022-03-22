expressao = str((input('Digite uma expressão com parenteses: ')))

l1 = 0
l2 = 0
pos = 0

while pos < len(expressao):
    if '(' in expressao[pos]:
        l1 += 1
    if ')' in expressao[pos]:
        l2 += 1
    pos += 1

if l1 == l2:
    print('A expressão está correta!')
else:
    print('A expressão está INCORRETA!')

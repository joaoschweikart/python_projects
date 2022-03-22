print('=-'*20)
print('BOLETIM ESCOLAR')
print('=-'*20)
listacompleta = []
listaalunos = []
cont = 0

while True:
    listaalunos.append(str(input('Nome do aluno: ')).upper().strip())
    listaalunos.append(float(input('Digite a 1º nota: ')))
    listaalunos.append(float(input('Digite a 2º nota: ')))
    listacompleta.append(listaalunos[:])
    listaalunos.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    cont = cont + 1
    if continuar == 'N':
        break

print('=-'*20)
print('BOLETIM DOS ALUNOS: ')
print('=-'*20)
print('Nº  NOME DO ALUNO     MÉDIA')

for l in range(0, cont):
    media = (listacompleta[l][1] + listacompleta[l][2])/2
    print(f'{l}   {listacompleta[l][0]:<15}    {media}')

while True:
    print('=-' * 30)
    l = int(input('De qual aluno você deseja visualizar as notas? (999 INTERROMPE): '))
    if l == 999:
        print('FINALIZANDO...')
        break
    print(f'Aluno: {listacompleta[l][0]}     Notas: {listacompleta[l][1]} e {listacompleta[l][2]}')

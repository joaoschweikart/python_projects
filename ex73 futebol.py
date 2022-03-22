
brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético Mineiro',
               'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Corinthians', 'Fluminense',
               'Ceará', 'Vasco da Gama', 'Sport Recife', 'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print('=-'*30)
print('A tabela do brasileirão, em ordem, está assim: ')
print(brasileirao)
print('=-'*30)
print('Esses são os 5 primeiros times:')
print(brasileirao[:5])
print('=-'*30)
print('Essa é a zona de rebaixamento: ')
print(brasileirao[-4:])
print('=-'*30)
print('Esses são os times em ordem alfabética: ')
print(sorted(brasileirao))
print('=-'*30)
print(f'A chapecoense está ná {brasileirao.index("Chapecoense")+1}ª posição.')
print('=-'*30)

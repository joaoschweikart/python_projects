galera = list()
pessoa = list()
for c in range(0, 5):
    pessoa.append(str(input('Digite um nome: ')).upper().strip())
    pessoa.append(int(input('Digite sua idade: ')))
    galera.append(pessoa[:])
    pessoa.clear()
print(galera)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

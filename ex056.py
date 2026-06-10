nomes = []
idades = []
sexos = []
for i in range(4):
    nome = input('Nome: ')
    nomes.append(nome)
    idade = int(input('idade: '))
    idades.append(idade)
    sexo = input('sexo(M ou F): ').upper()
    sexos.append(sexo)
print(f'A média de idades é {sum(idades)/len(idades)}')


import datetime
demaior = []
demenor = []
for i in range(7):
    idade = int(input('ano de nascimento: '))
    if datetime.datetime.now().year - idade  > 18:
        demaior.append(idade)
    else:
        demenor.append(idade)
print(demaior)
print(demenor)
print(datetime.datetime.now().year)
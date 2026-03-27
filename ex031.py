distancia = float(input('Qual a distancia em km da viagem? '))
if distancia <= 200:
    preço = distancia * 0.50
    print(f'O valor da passagem é R${preço}')
else:
    preço = distancia * 0.45
    print(f'O valor da passagem é R${preço}')
speed = float(input("Digite a velociade do carro: "))
if speed > 80.0:
    multa = (speed - 80) * 7
    print(f'Velocidade acima do limite. Multa R${multa}')
else:
    print('Velocidade regular')
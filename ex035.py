seg1 = float(input('Digite o primeiro segmento: '))
seg2 = float(input('Digite o segundo segmento: '))
seg3 = float(input('Digite o terceiro segmento: '))

if  seg1 + seg2 > seg3 and seg3 + seg2 > seg1 and seg3 + seg1 > seg2:
    print('é possivel formar um triangulo.')
else:
    print('não é possível formar um triangulo')
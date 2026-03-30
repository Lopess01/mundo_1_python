seg1 = float(input('Digite o primeiro segmento: '))
seg2 = float(input('Digite o segundo segmento: '))
seg3 = float(input('Digite o terceiro segmento: '))
forma_triangulo = seg1 + seg2 > seg3 and seg3 + seg2 > seg1 and seg3 + seg1 > seg2
if  forma_triangulo:
    print('é possivel formar um triangulo, e o triangulo formado é: ')
    if seg1 == seg2 and seg1 == seg3:
        print("      Triangulo equilátero".upper())
    elif seg1 == seg2 or seg2 == seg3 or seg1 == seg3:
        print('      Triangulo isóceles'.upper())
    else:
        print('      Triangulo escaleno'.upper())
else:
    print('não é possível formar um triangulo')

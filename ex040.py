n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
if (n1 + n2)/2 > 7:
    print('APROVADO')
elif (n1 + n2)/2 > 5 and (n1 + n2)/2 < 6.9:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')

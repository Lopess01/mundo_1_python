peso = float(input("Peso(Kg): "))
altura = float(input("Altura(M): "))
imc = peso / (altura * altura)
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 < imc < 25:
    print("Peso ideal")
elif 25 < imc < 30:
    print("Sobrepeso")
elif 30 < imc < 40:
    print("obesidade")
else:
    print("OBESIDADE MÓRBIDA")
numeros = [342,-23,1,2,4,-53,-1,5233,-3,77,3,-5]
posi = []
nega = []
for n in numeros:
    if n > 0:
        posi.append(n)
    else:
        nega.append(n)
print(posi, nega)
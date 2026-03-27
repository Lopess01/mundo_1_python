salario = float(input('Digite seu atual salário: '))
if salario > 1250.00:
    novo_salario = salario + (salario * 0.10)
    print(f"Seu salário foi ajustado com 10% de aumento para R${novo_salario}")
else:
    novo_salario = salario + (salario * 0.15)
    print(f"seu novo salario com 15% de aumento é R${novo_salario}")
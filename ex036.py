valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("em Quantos anos deseja pagar: "))
 
prestacao = valor_casa / (anos*12)
print(prestacao)
if salario * 0.30 > prestacao:
    print("Emprestimo aprovado!")
else:
    print("Emprestimo negado! a prestação passa de 30% do seu salario")
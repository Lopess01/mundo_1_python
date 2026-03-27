n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
'''if n1 > n2 and n1 > n3 :
    print(f'maior número: {n1}')
elif n2 > n1 and n2 > n3:
    print(f'maior número: {n2}')
elif n3 > n1 and n3 > n2:
    print(f'maior número: {n3}')
if n1 < n2 and n1 < n3 :
    print(f'menor número: {n1}')
elif n2 < n1 and n2 < n3:
    print(f'menor número: {n2}')
elif n3 < n1 and n3 < n2:
    print(f'menor número: {n3}')'''
menor = n1
if n2<n1 and n3>n2: menor = n2
if n3<n1 and n3<n2: menor = n3
maior = n1
if n2>n1 and n2>n3: maior = n2
if n3>n2 and n3>n1: maior = n3
print(f'''O maior número é {maior}
 e o menor número é {menor}''')
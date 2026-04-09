even = []
for i in range(6):
    n = int(input(f'Digite o {i+1}° número: '))
    if n % 2 == 0:
        even.append(n)
print(sum(even))

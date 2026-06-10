peso = []
x = 0
for i in range(5):
    peso1 =  float(input('Peso: '))
    peso.append(peso1)
for i in peso:
    if i > x:
        x = i
print(f'maior peso: {x}kg')
x = 1000
for i in peso:
    if i < x:
        x = i
print(f'menor peso: {x}kg')
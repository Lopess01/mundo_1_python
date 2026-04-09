primeiro_termo = int(input('1° Termo: '))
razao = int(input('Razão: '))
for i in range(10, 1, -1):
    termo = primeiro_termo + (i-1) * razao
    print(termo)
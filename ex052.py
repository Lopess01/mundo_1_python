n = int(input("Digite um número: "))
if n <= 1:
    x ="não primo"
elif n == 2:
    x = "é primo"
elif n > 2 and n % 2 == 0:
    x ='nao primo'
else:
    for i in range(2, n):
        if n % i == 0:
            x = 'não primo'
            break
        else:
            x = 'primo!!!!!'  
print(x)
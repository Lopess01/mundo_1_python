primo = True
n = int(input("Digite um número: "))
if n <= 1:
    print("não primo")
else:
    for i in range(2,n):
        print(f'{n} ÷ {i} = {n/i:.2f}')
        if n % i == 0:
            primo = False
            break
    if primo == True:
        print("primo")
    else:
        print('nao primo')    
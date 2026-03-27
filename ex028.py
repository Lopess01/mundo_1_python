import random
n = int(input('Digite um número de 0 a 5 '))
if n == random.randint(0,5):
    print('Parabéns, você adivinhou o número!')
else: 
    print("Errou! inicie novamente para acertar.")
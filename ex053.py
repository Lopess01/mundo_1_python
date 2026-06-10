palavra = input('Digite uma palavra: ').lower()
if palavra == palavra[::-1]:
    print(f'{palavra} é um palindromo')
else:
    print('não é palindromo')
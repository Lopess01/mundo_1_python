n = int(input('Digite um número: '))
base = int(input('''Você deseja converter o  número para qual base?
      [ 1 ] binário
      [ 2 ] hexadecimal
      [ 3 ] octal 
digite sua resposta: '''))
if base == 1:
    print(bin(n)[2:])
elif base == 2:
    print(hex(n)[2:])
else:
    print(oct(n)[2:])
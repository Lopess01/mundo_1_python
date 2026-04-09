valor = float(input('preço do produto: '))
forma_pagamento = int(input(''
    '                 [ 1 ] crédito\n'
    '                 [ 2 ] débito\n'
    '                 [ 3 ] pix\nopção de pagamento: '))
if forma_pagamento == 1:
     parcelamento = int(input(""
     "               [ 1 ] A vista\n"
     "               [ 2 ] parcelado\nselecione: "))
     if parcelamento == 1:
          desconto = valor - valor * 0.05
          print(f'O novo valor é R${desconto}.')
     else:
          vezes = int(input('quantas vezes deseja parcelar? '))
          if vezes <= 2:
               print(f'o valor é {vezes}x de R${valor/vezes:.2f}')
          elif vezes >= 3:
               juros = valor + valor * 0.20
               print(f'você irá pagar {vezes}x de {juros/vezes:.2f} com o total {juros}')  
elif forma_pagamento == 2:
     desconto = valor + valor * 0.05
     print(f'O novo valor é R${desconto}.')
elif forma_pagamento == 3:
     desconto = valor - valor * 0.10
     print(f'o valor com 10% de desconto é {desconto}')
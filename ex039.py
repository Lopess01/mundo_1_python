import datetime
ano_nascimento = int(input("ano de nascimento: ").capitalize())
ano = datetime.date.today().year
if ano - ano_nascimento == 18:
    print('Ano de alistamento, Aliste-se o mais rápido possivel.')
elif ano - ano_nascimento > 18 :
    alistamento = ano - ano_nascimento
    print(f'alistamento atrasado {(alistamento - 18)} anos, procure se alistar o mais rápido.')
else:
    alistamento = ano - ano_nascimento
    print(f'ainda não chegou sua hora, ainda faltam {18 - alistamento} anos')
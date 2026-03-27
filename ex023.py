n = input("Enter a number: ").zfill(4)
# o zfill garante que o numero tenha 4 digitos
print(f'''    Unit {n[-1]}
    tens: {n[-2]}
    hundreds: {n[-3]}
    thausands: {n[-4]}''')




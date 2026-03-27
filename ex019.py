import random
a1 = str(input("Enter the firts student: "))
a2 = str(input('Enter the second student: '))
a3 = str(input("Enter the third student: "))
a4 = str(input('Enter the fourth student: '))
list = [a1, a2, a3, a4]
print(f'the chosen student is {random.choice(list)}')
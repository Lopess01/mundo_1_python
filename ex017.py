import math
adjacent = float(input("Which is the adjacent side? "))
os = float(input('Which is the oppsite side? '))
hyp = math.hypot(adjacent, os)
print(f"The hypotenuse of the triangle is {hyp}")


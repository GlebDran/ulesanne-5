import math

N = float(input("Sisesta maatüki laius (m): "))
M = float(input("Sisesta maatüki pikkus (m): "))
diagonaal = math.sqrt(N**2 + M**2)
print(f"Maatüki diagonaal on {diagonaal:.2f} meetrit.")


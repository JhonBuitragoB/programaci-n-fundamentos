# Saber si un numero es PAR

# Variables
linea = "=" * 10
num = int(input("Ingrese un número: "))
num_par = num % 2 == 0

print(f"{num} es par: {num_par}")
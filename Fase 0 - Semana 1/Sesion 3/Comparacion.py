# Operadores de Comparación

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))
linea = "=" * 10

"""
Estas son las operaciones que realiza el programa
cada numero se evalua con el oparador de comparación
"""

igual_a = num1 == num2
distinto_de = num1 != num2
mayor_que = num1 > num2
menor_que = num1 < num2
mayor_o_igual = num1 >= num2
menor_o_igual = num1 <= num2

print("\n")
print(f"{linea} COMPARACIÓN {linea}\n")
print(f"{num1} es igual a {num2}: {igual_a}")
print(f"{num1} es distinto de {num2}: {distinto_de}")
print(f"{num1} es mayor que {num2}: {mayor_que}")
print(f"{num1} es menor que {num2}: {menor_que}")
print(f"{num1} es mayor o igual que {num2}: {mayor_o_igual}")
print(f"{num1} es menor o igual que {num2}: {menor_o_igual}")
print(f"\n{linea} FIN {linea}\n")


# Variables del programa
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2       # con decimales
div_ent = num1 // num2  # sin decimales
modulo = num1 % num2
potencia = num1 ** num2

# Salida por consola
print("=========\n")
print(f"Para los números: {num1} y {num2}\n")
print(f"La suma es : {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicación es: {multi}")
print(f"La division es: {div:.2f}")
print(f"La division sin decimales es: {div_ent}")
print(f"El residuo es: {modulo}")
print(f"La potencia es: {potencia}")
print("\n")



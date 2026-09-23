# Temperatura

temperatura = float(input("Ingrese la temperatura en Grados Celsius: "))
fahrenheit = temperatura * 9/5 + 32
mayor_que = fahrenheit > 100
linea = "*" * 10

print("\n")

print(f"La temperatura en Fahrenheites: {fahrenheit:.2f}")
print(f"\nLa temperatura es mayor a 100: {fahrenheit> 100}")
print(f"La temperatura es mayor que 100: {mayor_que}\n")
print(f"{linea} FIN {linea}")


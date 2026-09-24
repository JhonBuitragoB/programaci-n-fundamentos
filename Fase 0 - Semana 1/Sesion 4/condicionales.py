"""# PROGRAMA PARA CALCULAR EDAD

edad = int(input("Ingrese su edad: "))

if edad <13:
    print("Eres niño")
elif edad <18:
    print("Eres Adolescente")
elif edad >= 65:
    print("Eres Adulto Mayor")
else:
    print("Eres Adulto")



#PROGRAMA DE NOTAS

nota = float(input("Ingresa la Nota: "))

if nota < 60:
    print("Reprobado")
elif nota >= 60 and nota <=89:
    print("Aprobado")
else:
    print("Excelente")

    """
# RESPUESTA A PREGUNTA

respuesta = input("Tienes mas de 18 años?: (si/no): ")

if respuesta == "si":
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

    """
    Al escribir si o Si, o cualquier otra variante
    el programa siempre revisa la condición y si no es exactamente como dice allí
    toma el otro camino. Al escribir Si, imprime: Eres menor de edad
    """
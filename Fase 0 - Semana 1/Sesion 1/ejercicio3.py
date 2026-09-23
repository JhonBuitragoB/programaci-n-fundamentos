#=== FICHA ESTUDIANTE ===

nombre_completo = "Emilio"  # Cual es el estandar para escribir las variantes?
carrera = "Ingenieria Informática"
semestre = 5
promedio = 4.33 # Se hace con operación matemática o es un valor fijo
becado = False

print(f"Nombre del estudiante: {nombre_completo}\n"
      f"Carrera: {carrera}\nSemestre actual: {semestre}\n"
      f"Promedio: {promedio:.2f}\nBecado: {becado}"
      )
print("\n")
print("=== VARIABLES Y TIPOS ===\n")
print(f"Tipo: {type(nombre_completo)} || Dato almacenado: {nombre_completo}")
print(f"Tipo: {type(carrera)} || Dato almacenado: {carrera}")
print(f"Tipo: {type(semestre)} || Dato almacenado: {semestre}")
print(f"Tipo: {type(promedio)} || Dato almacenado: {promedio}")
print(f"Tipo: {type(becado)} || Dato almacenado: {becado}\n")


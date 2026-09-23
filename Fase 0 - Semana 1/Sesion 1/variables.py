name = "Jhon" 
age= 40
altura= 1.70
ciudad= "Bogotá" #comentario
estudiante= True

# Para comentar se usa el símbolos numeral

print(f"nombre: {name}\nedad: {age}\n"
      f"estatura: {altura:.2f}\n"
      f"es estudiante activo? {estudiante}"
      )
print(f"\nHola mi nombre es {name} soy de {ciudad} y tengo {age} años")
print("\n=== Tipos de Variables===\n")

print(type(name),"almacenan texto")
print(type(age),"almacenan numeros enteros")
print(type(altura),"Almacenan nuneros con decimales")
print(type(estudiante),"Almacenan booleanos, false o True")
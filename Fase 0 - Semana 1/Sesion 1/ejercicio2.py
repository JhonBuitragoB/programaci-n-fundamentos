# === MASCOTAS ====

nombre= "Nacho"
raza = "Frensh Pudell"
edad = 10
color = "Blanco"
peso = 8.55
genero = "Macho"
vacunado = True

print(f"El nombre de este perrito es: {nombre}\n"
      f"de la Raza: {raza}\nSu edad es: {edad} años\n"
      f"Su color es: {color}\nY su peso: {peso:.2f} kilos\n"
      f"Está vacunado: {vacunado}\n"
      )

print(f"nombre: {nombre} {type(nombre)}")
print(f"raza: {raza} {type(raza)}")
print(f"edad: {edad} {type(edad)}")
print(f"color: {color} {type(color)}")
print(f"peso: {peso} {type(peso)}")
print(f"genero: {genero} {type(genero)}")
print(f"vacunado: {vacunado} {type(vacunado)}")

#resultado = "Cinco" * "Cinco"   # str * str, ¿funciona o falla?
#resultado2 = 2.5 * "Cinco"      # float * str, ¿funciona o falla?

#El código falla porque * repite cuando es un string con un entero
# float * string falla
# string * string falla
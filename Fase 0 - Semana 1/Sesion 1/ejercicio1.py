
# Ficha Producto

nombre_producto = 'Gorra'
precio = 25500.27
stock = 23
disponible = True
cantidad = "cinco"
precio_unitario = 10
total = precio_unitario * cantidad

print(f"Producto: {nombre_producto}\nprecio: ${precio:.2f}\nstock: {stock}\nDisponible: {disponible}")
print(total)
print(f"Precio:{precio}")
print(f"Precio:{precio:.2f}")

# Me sorprendio, pensé que saldria un error
# vi que repitio imprimio la cantidad en string las veces que tiene
# precio unitario, es decir 10 veces la palabra Cinco.

print(f"\nLa variable es tipo: {type(nombre_producto)}")
print(f"La variable es tipo: {type(precio)}")
print(f"La variable es tipo: {type(stock)}")
print(f"La variable es tipo: {type(disponible)}")

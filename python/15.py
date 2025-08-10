precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
precio_final = precio - (precio * descuento / 100)
print("El precio final es:", precio_final)
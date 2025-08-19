# 11. Desarrolla un algoritmo que verifique si la temperatura de una habitación está dentro de
# un rango aceptable (por ejemplo, entre 20°C y 25°C).

temperatura = float(input("Digite la temperatura de la habitaciónen grados: "))

if 20 <= temperatura <= 25:
    print(f"Temperatura actual: {temperatura}. Esta temperatura es aceptable")
else:
    print(f"Temperatura actual: {temperatura}. Esta temperatura no es aceptable")  vc
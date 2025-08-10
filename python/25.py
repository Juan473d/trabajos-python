total = 0
while True:
    num = int(input("Ingrese un número (0 para salir): "))
    if num == 0:
        break
    total += num
print("La suma total es:", total)
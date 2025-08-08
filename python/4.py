# Escribe un algoritmo que calcule el IMC de una persona a partir de su peso (kg) y altura (metros).

def calcular_imc(peso,altura):
    return peso / (altura ** 2)

def clasificar_imc(imc):
    if imc < 7 or imc > 70:
        return "Imposible"
    elif 7 <= imc < 18.5 :
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad grado 1"
    elif 35 <= imc < 40:
        return "Obesidad grado 2"
    elif 40 <= imc < 70:
        return "Obesidad grado 3"

def main():
    print("=== CALCULADOR DE IMC ===")
    print("\n === BIENVENIDO ===\n")

    while True:
        try:
            peso_persona = float(input("\n Por favor ingrese el peso de la persona en kg (0 para salir): "))
            if peso_persona == 0:
                print("Muchas gracias por utilizar nuestro programa, !VUELVE PRONTO¡") 
                break

            altura_persona = float(input("\n Ingrese la altura de a persona en metros (0 para salir): "))
            if altura_persona == 0:
                print("Muchas gracias por utilizar nuestro programa, !VUELVE PRONTO¡") 
                break
             
            conversion_imc = calcular_imc(peso_persona,altura_persona)
            clasificacion = clasificar_imc(conversion_imc)
            print(f"\n Su imc es: {conversion_imc:.2f} Calificación: {clasificacion}")

            continuar = input("\n Desea hacer otro calculo de imc? (si/no): \n").strip().lower()
            if continuar != "si":
                print("\n Muchas gracias por utilizar nuestro programa, !VUELVE PRONTO¡ \n")
                break
        
        except ValueError:
            print("\n Por favor ingrese un dato valido \n")

if __name__ == "__main__":
    main()


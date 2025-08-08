# Desarrolla un algoritmo que calcule la propina y el total a pagar en un restaurante, dado el monto de la cuenta y el porcentaje de propina.

def calcular_propina(monto, porcentaje):
    return (monto * porcentaje) / 100

def main():
    while True:
        try:
            monto_cuenta = float(input("Ingrese el monto de la cuenta o presione 0 para salir: $"))
            
            if monto_cuenta == 0:
                print("Gracias por utilizar nuestro programa, hasta la próxima :)")
                break
            elif monto_cuenta <= 5000:
                print("Ingrese un monto válido")
                continue
                
            porcentaje_propina = float(input("Ingrese el porcentaje de la propina: %"))
            propina = calcular_propina(monto_cuenta, porcentaje_propina)
            total = monto_cuenta + propina
            
            print(f"La propina que debe pagar es de: ${propina:.2f}")
            print(f"El total que debe de pagar es: ${total:.2f}")
            
            continuar = input("¿Desea calcular otra cuenta? (si/no): ").strip().lower()
            if continuar != "si":
                print("Gracias por utilizar nuestro programa")
                break
        except ValueError:
            print("Error: Por favor ingrese un valor numérico válido.")

if __name__ == "__main__":
    main()

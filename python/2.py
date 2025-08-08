# Crea un algoritmo que convierta de dólares a euros.

TASA_EURO = 0.859

def convertir_dolares_a_euros(dolares):
    return TASA_EURO * dolares

def mostrar_mensaje_despedida():
    print("Gracias por utilizar nuestro programa. ¡Hasta la próxima!")

def main():
    print("=== CONVERSOR DE DÓLARES A EUROS ===")
    
    while True:
        try:
            dolares_monto = float(input("Ingrese cantidad de dólares a convertir (0 para salir): $"))
            
            if dolares_monto == 0:
                mostrar_mensaje_despedida()
                break
                
            conversion = convertir_dolares_a_euros(dolares_monto)
            print(f"Su conversión da un total de: €{conversion:.2f}")
            
            continuar = input("¿Desea hacer otra conversión? (si/no): ").strip().lower()
            if continuar != "si":
                mostrar_mensaje_despedida()
                break
                
        except ValueError:
            print("Error: Por favor ingrese un valor numérico válido.")

if __name__ == "__main__":
    main()

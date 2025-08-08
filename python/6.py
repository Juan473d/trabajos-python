# 6. Diseña un algoritmo que calcule el costo total de un viaje, sumando el costo del
# combustible, el peaje y el alojamiento.

def mostrar_menu():
    print("""
==== CALCULADORA DE COSTOS DE VIAJE ====
         BIENVENIDO AL PROGRAMA
1. Calcular costo total del viaje
2. Salir del programa
""")


def calcular_costo_viaje(combustible: float, peaje: float, alojamiento: float) -> float:
    return combustible + peaje + alojamiento


def solicitar_float(mensaje: str) -> float:
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Por favor, ingrese un número positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Intente de nuevo con un número.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ").strip()

        if opcion == "1":
            combustible = solicitar_float("Ingrese el total gastado en combustible: ")
            peaje = solicitar_float("Ingrese el total gastado en peajes: ")
            alojamiento = solicitar_float("Ingrese el total gastado en alojamiento: ")

            total = calcular_costo_viaje(combustible, peaje, alojamiento)
            print(f"\n💰 El costo total de su viaje es: ${total:.2f}")

            continuar = input("\n¿Desea hacer otro cálculo? (si/no): ").strip().lower()
            if continuar != "si":
                print("\n¡Gracias por usar la calculadora! 👋")
                break

        elif opcion == "2":
            print("\n¡Hasta pronto! 👋")
            break
        else:
            print("\n❌ Opción inválida. Elija 1 o 2.")


if __name__ == "__main__":
    main()






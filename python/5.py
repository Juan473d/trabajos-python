# Desarrolla un algoritmo que permita agregar, eliminar y mostrar una lista de compras

def mostrar_menu():
    print("""
===== MENÚ LISTA DE COMPRAS =====
1. Agregar producto
2. Eliminar producto
3. Ver lista de compras
4. Salir
""")

def mostrar_lista(lista):
    if not lista:
        print("\nLa lista de compras está vacía.")
    else:
        print("\nLista de compras: ")
        for i, producto in enumerate(lista, start=1):
            print(f"{i} | {producto}")

def main():
    lista_compras = []

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == "1":
            producto = input("\nIngrese el nombre del producto que desea agregar: ")
            if producto:
                lista_compras.append(producto)
                print(f"\n'{producto}' ha sido agregado a la lista")
            else:
                print("No se ingresó ningún producto.")

        elif opcion == "2":
            if not lista_compras:
                print("\nNo hay productos para eliminar.")
            else:
                mostrar_lista(lista_compras)
                try:
                    indice = int(input("Ingrese el número del producto a eliminar: "))
                    if 1 <= indice <= len(lista_compras):
                        eliminado = lista_compras.pop(indice - 1)
                        print(f"\n'{eliminado}' fue eliminado exitosamente.")
                    else:
                        print("\nNúmero fuera de rango.")
                except ValueError:
                    print("\nPor favor, ingrese un número válido.")

        elif opcion == "3":
            mostrar_lista(lista_compras)

        elif opcion == "4":
            print("\n¡GRACIAS POR UTILIZAR EL PROGRAMA!")
            break

        else:
            print("\nOpción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()




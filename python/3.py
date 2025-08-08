# Implementa un algoritmo que clasifique a una persona en "Niño"(13), "Adolescente"(18), "Adulto" (+18) o "Adulto mayor"(65) según su edad

def clasificar_persona(edad):
    if 1 <= edad <= 3:
        return "La persona es un bebé."
    elif 4 <= edad <= 13:
        return "La persona es un niño."
    elif 14 <= edad <= 17:
        return "La persona es un adolescente."
    elif 18 <= edad <= 64:
        return "La persona es un adulto."
    elif 65 <= edad <= 129:
        return "La persona es un adulto mayor, ya va pal cajón :/"
    elif 130 <= edad:
        return "Lo sentimos, ya no hay persona solo huesos"
    else:
        return "Edad no válida"

def main():
    while True:
        try:
            edad = int(input("\nIngresa la edad o presiona 0 para salir: "))
            
            if edad == 0:
                print("Gracias por utilizar nuestro programa. Hasta la próxima.")
                break
                
            resultado = clasificar_persona(edad)
            print(resultado)
            
            continuar = input("¿Desea calcular otra edad? (si/no): ").strip().lower()
            if continuar != "si":
                print("Gracias por utilizar nuestro programa, vuelve pronto :)")
                break
        except ValueError:
            print("Error: Por favor ingrese un valor numérico válido.")

if __name__ == "__main__":
    main()
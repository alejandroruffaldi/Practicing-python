def opcion_escala(opcion, grados):
    ans = 0 
    
    if opcion == 'celsius':
        ans = grados * 9.0 / 5.0 + 32.0
    elif opcion == 'Fahrenheit':
        ans = (grados - 32.0) * 5.0 / 9.0
     
    return ans

def main():
    escala = input('Ingrese escala de origen (celsius/Fahrenheit), o escriba "salir" para terminar: ')
    while escala != 'salir':
        try:
            grados = float(input('Ingrese grados a convertir: '))
            if escala == 'celsius':
                print(f"{grados} grados Celsius equivalen a {opcion_escala(escala, grados):.2f} grados Fahrenheit")
            elif escala == 'Fahrenheit':
                print(f"{grados} grados Fahrenheit equivalen a {opcion_escala(escala, grados):.2f} grados Celsius")
            else:
                print("Opción inválida. Ingrese 'celsius' o 'Fahrenheit'.")
        except ValueError:
            print("Ocurrió un error. Ingrese un valor numérico válido.")
        escala = input('Ingrese escala de origen (celsius/Fahrenheit), o escriba "salir" para terminar: ')

if __name__ == "__main__":
    main()

            

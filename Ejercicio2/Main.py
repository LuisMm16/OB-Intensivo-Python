def main():
    """
    Aplicacion de agenda telefonica gestionada por consola
    """
    contactos = {}
    while True:
        print("¿Qué desea hacer?\nAgregar un contacto: 1\nBuscar un contacto: 2\nCerrar la aplicacion: 9")
        num = int(input())
        if num == 9:
            break
        elif num == 1:
            nombre = input("Ingrese el nombre del contacto: ")
            numero = input("Ingrese el número de teléfono: ")
            try:
                # Agrega un contacto al diccionario con el nombre ingresado
                contactos[f'{nombre}'] = int(numero)
                print(f'Agregado {nombre}: {numero}')
                print('==================================================')
            except ValueError:
                print('Ingrese un número válido')
                print('==================================================')
        elif num == 2:
            buscado = input("Nombre del contacto: ")
            # Iteracion para buscar los coincidentes mediante las keys del diccionario
            for name in list(contactos.keys()):
                # lower utilizado para coincidir asi esten escrito en combinacion de mayusculas y minusculas
                if name.lower().startswith(buscado.lower()):
                    print(name, contactos.get(name))
            print('==================================================')
        else:
            print('Ingrese una opción válida')
            print('==================================================')

if __name__ == '__main__':
    print("Bienvenido a tu agenda por consola")
    main()

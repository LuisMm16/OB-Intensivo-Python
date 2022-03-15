def calcular_primos(n):
    """
    Calcular los números primos entre 1 y n
    """
    lista_primos = []
    try:
        if n >= 1:
            for numero in range(1, n + 1):
            # Si el numero es dos (primo)
                if numero == 1:
                    continue
                elif numero == 2:
                    lista_primos.append(numero)
            # Si un numero es par (no primo), no se agrega
                elif numero % 2 == 0:
                    continue
                else:
                    # Contador para verificar las veces que no se cumplio la condicion if numero % i == 0
                    counter = 0
                    for i in range(3, numero, 2):
                        if numero % i == 0:
                            break
                        counter += 1
                    if counter == len(range(3, numero, 2)):
                        lista_primos.append(numero)
            return lista_primos
        else:
            raise ValueError

    except ValueError:
        print('Ingrese un número válido mayor o igual a 1')

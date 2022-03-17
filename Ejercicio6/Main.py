def encrypt(password):
    """
    Encriptar una contraseña de entre 6 y 12 caracteres devolviendo un string
    con 32 caracteres
    """
    if 6 <= len(password) <= 12:
        lista = [char for char in password]
        lista.append(lista[0])
        encrypted = crypt(lista)
        return encrypted
    else:
        return 'Ingrese una contraseña de entre 6 y 12 caracteres'


def crypt(lista):
    import random
    abc = 'abcdefghijklmnñopqrstuvwxyz0123456789'
    mydict = {}
    count = 1
    encrypt_pass = []
    for letter in abc:
        mydict[f'{letter}'] = count
        count += 1
    for i in range(len(lista) - 1):
        # Seleccionar el numero asociado al caracter actual del dict
        if lista[i] in abc:
            temp1 = mydict[f'{lista[i]}']
        else:
            temp1 = -1

        # Seleccionar el numero asociado al siguiente caracter del dict
        if lista[i + 1] in abc:
            temp2 = mydict[f'{lista[i + 1]}']
        else:
            temp2 = -1

        if temp1 + temp2 <= len(abc):
            encrypted = get_key(temp1 + temp2, mydict)
            # Para generar numeros pseudo aleatorios
            random.seed(temp1)
            rand_number1 = random.random()
            random.seed(temp2)
            rand_number2 = random.random()
            encrypt_pass.append(encrypted)
            if len(lista) - 1 == 6:
                encrypt_pass.append(str(rand_number1 + rand_number2)[2:6])
            elif len(lista) - 1 == 7:
                encrypt_pass.append(str(rand_number1 + rand_number2)[2:5])
            elif len(lista) - 1 == 8:
                encrypt_pass.append(str(rand_number1 + rand_number2)[2:5])
            elif len(lista) - 1 == 9:
                encrypt_pass.append(str(rand_number1 + rand_number2)[2:4])
            elif len(lista) - 1 == 10:
                encrypt_pass.append(str(rand_number1 + rand_number2)[2:4])
            elif len(lista) - 1 == 11:
                encrypt_pass.append(str(rand_number1 + rand_number2)[2:3])
            elif len(lista) - 1 == 12:
                encrypt_pass.append(str(rand_number1 + rand_number2)[2:3])

        else:
            encrypted = get_key(abs(temp1 - temp2), mydict)
            random.seed(temp1)
            rand_number1 = random.random()
            random.seed(temp2)
            rand_number2 = random.random()
            encrypt_pass.append(encrypted)
            if len(lista) - 1 == 6:
                encrypt_pass.append(str(rand_number1+rand_number2)[2:6])
            elif len(lista) - 1 == 7:
                encrypt_pass.append(str(rand_number1 + rand_number2)[2:5])
            elif len(lista) - 1 == 8:
                encrypt_pass.append(str(rand_number1 + rand_number2)[2:5])
            elif len(lista) - 1 == 9:
                encrypt_pass.append(str(rand_number1 + rand_number2)[2:4])
            elif len(lista) - 1 == 10:
                encrypt_pass.append(str(rand_number1 + rand_number2)[2:4])
            elif len(lista) - 1 == 11:
                encrypt_pass.append(str(rand_number1 + rand_number2)[2:3])
            elif len(lista) - 1 == 12:
                encrypt_pass.append(str(rand_number1 + rand_number2)[2:3])

    for x in range(32 - len(''.join(encrypt_pass))):
        random.seed(temp1 * temp2 + x)
        encrypt_pass.append(str(random.random())[2:3])
    return ''.join(encrypt_pass)


def get_key(wanted, mydict):
    """
    Obtener la key a partir del valor deseado del dict
    """
    for key, value in mydict.items():
        if wanted == value:
            return key


pass_original = 'asgahf2@gfgr'
print('Pass original:', pass_original)
print(encrypt(pass_original))
print("Longitud:", len(encrypt(pass_original)))

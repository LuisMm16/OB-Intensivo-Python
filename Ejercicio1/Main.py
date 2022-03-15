def main():
    """
    Imprimir todos los ficheros existentes en la carpeta Descargas
    """
    import os
    from Operations import get_files_name_size

    # Cambiar de directorio
    # os.chdir('C:\\Users\\Luis\\Downloads')

    # Para listar todo en el directorio
    # all_files = os.listdir(path='.')

    # Para escanear todo el directorio (incluye el tipo de archivo)
    all_archives = os.scandir(path='C:\\Users\\Luis\\Downloads')

    #Imprimir el nombre y tamaño del archivo
    get_files_name_size(all_archives)

    # Recorrer de forma recursiva utilizando os.walk
    all_directories = os.walk(top='C:\\Users\\Luis\\Downloads')
    for directory in all_directories:
        all_archives = os.scandir(directory[0])
        print("Contenido de la dirección:", directory[0])
        get_files_name_size(all_archives)


if __name__ == "__main__":
    main()
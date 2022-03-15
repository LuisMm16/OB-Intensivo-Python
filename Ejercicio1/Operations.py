import math
import os


def converter(cantidad):
    """
    Convertir Bytes a MB
    """
    cantidad /= 1024

    if cantidad > 1024:
        cantidad /= 1024
        return str(round(cantidad, 2)) + " MB"
    return str(math.floor(cantidad)) + " KB"


def get_files_name_size(all_archives):
    """
    Imprimir el nombre y tamaño de los archivos por consola
    """
    for archive in all_archives:
        if archive.is_file():
            peso = os.stat(archive).st_size
            print("Nombre del archivo:", archive.name)
            print("Tamaño:", converter(peso))
    return None

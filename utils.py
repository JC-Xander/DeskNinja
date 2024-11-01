"""Modulos con funcione extrar que se utilizaran para el ordenamiento de los archivos del escritorio."""

import os
import re
import shutil
from givecolor import Fore

def file_exist(file_path:os.path, filename:str, text:str='_ext') -> os.path:
    """Verifica si el archivo o carpeta que se va a mover existe en la ruta especificada. En caso de que exista, esta funcion añadira un texto extra hasta que genere uno nombre unico para el archivo o directorio.
    Args:
        file_path (str): La ruta donde se va a mover el archivo o carpeta.
        filename (str): El nombre del archivo o carpeta que se va a mover.
        text (str): Texto extra que se añadira al nombre del archivo o carpeta.
        
    return:
        path : Ruta completa del archivo o carpeta con el nombre unico."""
    path = os.path.join(file_path, filename)

    # Verifica si la ruta existe, en caso de no existir la retorna
    if not os.path.exists(path):
        return path
    
    # Si la ruta existe, se le agrega @text al nombre hasta que sea unico
    name, extension = os.path.splitext(filename)
    return file_exist(file_path, f"{name}_copy{extension}", text)

# /------------------------------------------------------------------------/

def verificate_file(dir_path:os.path, regular_expression:re) -> bool:
    """Verifica si existe un archivo o directorio con las especificacione dadas en @regular_expression
    Args:
        dir_path (path): Directorio donde se realizara la busqueda
        regular_expression (re): Expresion regular que se utilizara para buscar un archivo o directorio con nombre coincidente.
    return:
        bool : True si existe un archivo o directorio con el nombre coincidente, False en caso contrario."""
    
    if os.path.isdir(dir_path):
        for file in os.listdir(dir_path):
            if re.search(regular_expression, file):
                return True
    else:
        raise NotADirectoryError(f"{dir_path} is not a valid directory")
    
    return False

# /------------------------------------------------------------------------/

def mv_file(file_path:os.path, new_path:os.path, file_name:str='file') -> None:
    def mv_file(file_path: os.path, new_path: os.path, file_name: str = 'file') -> None:
        """Mueve un archivo de una ruta a otra, creando los directorios necesarios si no existen.
        Args:
            file_path (os.path): La ruta del archivo que se va a mover.
            new_path (os.path): La nueva ruta donde se moverá el archivo.
            file_name (str): El nombre del archivo (opcional, por defecto 'file')."""
    
    # Creando los directorios intermedios si no existen
    directory = os.path.dirname(new_path)
    os.makedirs(directory, exist_ok=True)
    try:
        shutil.move(file_path, new_path)
    except PermissionError:
        print(f"\tError: No se tiene permisos para mover {file_name}", fore=Fore.RED)
    print(f">> {file_name} -> {new_path}", fore=Fore.GREEN)


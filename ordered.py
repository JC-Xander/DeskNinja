"""Ordenador de todos los archivos del escritorio"""

import os
import re
from config import PATHS # Importando las rutas de los directorios
from config import (
    PAC_UNAH,
    ACCOUNT
)
from utils import (
    file_exist,
    verificate_file,
    mv_file
)

def classify_and_move_file(file_name:os.path) -> os.path:
    """Clasifica un archivo según su nombre y extensión y determina la nueva ruta."""
    if re.search(rf"({ACCOUNT}|unah|{re.escape(PAC_UNAH)})", file_name, re.IGNORECASE):
        return file_exist(PATHS['UNIVERSITY'], file_name)

    extension = re.search(r"\.(\w+)$", file_name)
    if extension:
        ext = extension.group(1).lower()
        for category, ext_list in EXTENSIONS.items():
            if ext in ext_list:
                return file_exist(PATHS[category], file_name)
            
    return file_exist(PATHS['DEFAULT'], file_name)

def classify_and_move_dir(dir_path:os.path, dir_name) -> os.path:
    """Clasifica un directorio según su nombre y determina la nueva ruta."""
    # Directorios
    if verificate_file(dir_path, r'.git'):
        return file_exist(PATHS['REPOSITORIE'], dir_name)
    else:
        return file_exist(PATHS['DEFAULT'], dir_name)

EXTENSIONS = {
    'PICTURE': ['jpg', 'png', 'jpeg'],
    'PDF': ['pdf'],
    'WORD': ['doc', 'docx'],
    'PRESENTATION': ['ppt', 'pptx'],
    'COMPRESSED': ['zip', 'rar', '7z', 'tar', 'gz'],
    'CODE': ['py', 'js', 'html', 'css', 'php', 'java', 'c', 'cpp', 'cs', 'rb', 'go', 'cpp', 'md'],
    'EXCEL': ['xls', 'xlsx']
}

file_ignore = ['desktop.ini', 'Thumbs.db', 'compressed', 'No Organizados']

if __name__ == '__main__':
    # Iterar sobre los archivos y directorios del escritorio  
    for file_name in os.listdir(PATHS['DESKTOP']):

        # path del archivo o directorio actual
        file_path = os.path.join(PATHS['DESKTOP'], file_name)
        # path donde se moverá 
        new_path = None

        # Organizando archivos
        if file_name in file_ignore: continue
        if os.path.isfile(file_path):
            new_path = classify_and_move_file(file_name)
        else:
            new_path = classify_and_move_dir(file_path, file_name)

        # Mover el archivo al nuevo path
        if new_path:
            mv_file(file_path, new_path, file_name)

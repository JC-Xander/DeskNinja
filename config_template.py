import os
import datetime

# Variables constantes
DATE = datetime.datetime.now().strftime('%Y-%m-%d')
PAC_UNAH = 'III_XXXX'  # Reemplaza con tu PAC de la universidad
ACCOUNT = 'TU_NUMERO_DE_CUENTA'  # Reemplaza con tu número de cuenta

# Rutas  
user_path = os.path.expanduser("~")  # Ruta del usuario actual

# Rutas de guardado (reemplaza con las rutas específicas de tu sistema)
desktop_path = os.path.join(user_path, 'Desktop')  # Ruta al escritorio
picture_path = os.path.join(user_path, 'Imagenes')  # Ruta a imágenes
unah_path = os.path.join(user_path, 'Universidad', PAC_UNAH)  # Ruta a los documentos de la universidad
pdf_path = os.path.join(user_path, 'Documentos', 'PDFs')  # Ruta para PDFs
word_path = os.path.join(user_path, 'Documentos', 'Word')  # Ruta para documentos de Word
powerPoint_path = os.path.join(user_path, 'PowerPoint')  # Ruta para PowerPoint
compressed_path = os.path.join(user_path, 'Desktop', 'compressed')  # Ruta para archivos comprimidos
code_path = os.path.join(user_path, 'Documentos', DATE)  # Ruta para archivos de código, con fecha actual
git_path = os.path.join(user_path, 'Documentos', 'GitHub')  # Ruta para repositorios de Git
default_path = os.path.join(user_path, 'Desktop', 'No Organizados')  # Ruta para archivos sin clasificar

# Diccionario de rutas
PATHS = {
    "USER": user_path,
    "DESKTOP": desktop_path,
    "PICTURE": picture_path,
    "UNIVERSITY": unah_path,
    "PDF": pdf_path,
    "WORD": word_path,
    "PRESENTATION": powerPoint_path,
    "COMPRESSED": compressed_path,
    "CODE": code_path,
    "REPOSITORIE": git_path,
    "DEFAULT": default_path
}

#!/usr/bin/python3
""" 
This script adds all arguments passed to it from the command line to a Python list, 
and then saves them to a file in JSON format. 
"""

# Importamos los módulos necesarios
import sys  # Importamos el módulo sys para manejar los argumentos de la línea de comandos
import os   # Importamos el módulo os para manejar operaciones del sistema operativo
""" json"""
# Importamos las funciones necesarias desde otros módulos
from save_to_json_file import save_to_json_file  # Importamos la función para guardar datos en un archivo JSON
from load_from_json_file import load_from_json_file  # Importamos la función para cargar datos desde un archivo JSON
"""json"""
# Definimos el nombre del archivo donde se guardarán los datos
filename = "add_item.json"
"""json"""
# Obtenemos todos los argumentos pasados al script desde la línea de comandos, excluyendo el nombre del script
args = sys.argv[1:]
"""json"""
# Verificamos si el archivo JSON ya existe
if os.path.exists(filename):
    # Si el archivo existe, cargamos su contenido (debería ser una lista) utilizando la función load_from_json_file
    items = load_from_json_file(filename)
else:
    # Si el archivo no existe, inicializamos una lista vacía para almacenar los elementos
    items = []

# Añadimos los argumentos de la línea de comandos a la lista cargada o a la lista vacía
items.extend(args)

# Guardamos la lista actualizada en el archivo JSON utilizando la función save_to_json_file
save_to_json_file(items, filename)


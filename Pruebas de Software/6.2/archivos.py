"""
Pruebas unitarias
"""
import os
import json


class Archivos:
    """Definiendo la clase Archivos"""

    # Definición de métodos
    @staticmethod
    def get_next_id_from_file(prefix):
        """Método para obtener el siguiente ID para un prefijo dado"""

        files = os.listdir("./archivos")

        # Obtener los números que ya existen
        numbers = []
        for file in files:
            file_name, _file_extension = os.path.splitext(file)
            part = file_name.replace(prefix, '')
            if part.isdigit():
                numbers.append(int(part))

        # If there are no numeric parts in filenames
        if not numbers:
            return 1
        return max(numbers)+1

    @staticmethod
    def to_json(obj):
        """Método para imprimir los datos de la clase a Json"""
        return json.dumps(obj.__dict__)

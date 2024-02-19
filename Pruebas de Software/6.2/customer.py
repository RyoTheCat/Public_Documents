"""
Pruebas unitarias
"""
import json
import os

from archivos import Archivos


class Customer:
    """Definiendo la clase Customer"""

    # Definición de atributos
    obj_id = -1
    first_name = ""
    last_name = ""
    city = ""
    prefix = "./archivos/C"

    # Definición de métodos
    def __init__(self, obj_id, first_name, last_name, city):
        """Constructor de la clase"""
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        if -1 == obj_id:
            self.obj_id = self.get_next_id()
        else:
            self.obj_id = obj_id

    def guardar(self):
        """Método Guardar"""
        with open(f"{self.prefix}{self.obj_id :02d}.txt", "w",
                  encoding='utf-8') as f:
            f.write(Archivos.to_json(self))

    def borrar(self):
        """Método Borrar"""
        try:
            os.remove(f"{self.prefix}{self.obj_id :02d}.txt")
        except FileNotFoundError:
            print(f"El Cliente {self.obj_id} no se puede borrar")

    def load(self, obj_id):
        """Método para cargar un objeto"""
        filename = f"{self.prefix}{obj_id :02d}.txt"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                customer = Customer.from_dict(data)
                f.close()
                return customer
        except FileNotFoundError:
            print(f"Cliente {obj_id} no encontrado")
            return None

    def get_next_id(self):
        """Método generar nuevo ID"""
        return Archivos.get_next_id_from_file("C")

    def imprimir_detalle(self):
        """Método desplegar información"""
        print(f"Cliente '{self.first_name}': {self.last_name} "
              f"- {self.city}")

    @classmethod
    def from_dict(cls, dt):
        """Método para crear un objeto desde un diccionario"""
        return cls(dt['obj_id'], dt['first_name'], dt['last_name'],
                   dt['city'])

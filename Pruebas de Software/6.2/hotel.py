"""
Pruebas unitarias
"""
import json
import os
from archivos import Archivos


class Hotel:
    """Definiendo la clase Hotel"""

    # Definición de atributos
    obj_id = -1
    resort_name = "MiHotel"
    type_obj = "Turismo"
    rooms = 10
    prefix = "./archivos/H"

    # Definición de métodos
    def __init__(self, obj_id, resort_name, type_obj, rooms):
        """Constructor de la clase"""
        self.resort_name = resort_name
        self.type_obj = type_obj
        self.rooms = rooms
        if -1 == obj_id:
            self.obj_id = self.get_next_id()
        else:
            self.obj_id = obj_id
        print(f"Instancia Hotel {self.resort_name}")

    def guardar(self):
        """Método Guardar"""
        with open(f"{self.prefix}{self.obj_id :02d}.txt", "w",
                  encoding='utf-8') as f:
            f.write(Archivos.to_json(self))

    def borrar(self):
        """Método Borrar"""
        try:
            os.remove(f"{self.prefix}{self.obj_id :02d}.txt")
            print(f"Instancia Hotel {self.resort_name} borrada")
        except FileNotFoundError:
            print(f"La instancia {self.obj_id} no se pudo borrar")

    def load(self, obj_id):
        """Método de lectura del objeto"""
        filename = f"{self.prefix}{obj_id :02d}.txt"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                hotel = Hotel.from_dict(data)
                f.close()
                return hotel
        except FileNotFoundError:
            print(f"Hotel {obj_id} no fue posible leerlo")
            return None

    def get_next_id(self):
        """Método para generar el ID"""
        return Archivos.get_next_id_from_file("H")

    def imprimir_detalle(self):
        """Método para desplegar informaciòn"""
        print(f"Hotel {self.resort_name}, {self.type_obj}")

    @classmethod
    def from_dict(cls, dt):
        """Método para crear el objeto"""
        return cls(dt['obj_id'], dt['resort_name'],
                   dt['type_obj'], dt['rooms'])

    @classmethod
    def create_reservation(cls, reservation):
        """Método para guardar una reservación"""
        with open(f"{cls.prefix}res{reservation.hotel_id :02d}"
                  f"_{reservation.customer_id}.txt", "w", encoding='utf-8') \
                as f:
            f.write(Archivos.to_json(reservation))

    @classmethod
    def cancel_reservation(cls, reservation):
        """Método para cancelar una reservación"""
        try:
            os.remove(f"{cls.prefix}res{reservation.hotel_id :02d}"
                      f"_{reservation.customer_id}.txt")
        except FileNotFoundError:
            pass

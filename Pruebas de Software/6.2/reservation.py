"""
Pruebas unitarias
"""
import json
import os
from hotel import Hotel
from archivos import Archivos


class Reservation:
    """Definiendo la clase Reservación"""

    # Definición de atributos
    obj_id = -1
    customer_id = -1
    hotel_id = -1
    prefix = "./archivos/R"

    # Definición de métodos
    def __init__(self, obj_id, customer_id, hotel_id, room):
        """Constructor de la clase"""
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.room = room
        if -1 == obj_id:
            self.obj_id = self.get_next_id()
        else:
            self.obj_id = obj_id

    def guardar(self):
        """Método para guardar en archivo la información de la clase"""
        with open(f"{self.prefix}{self.obj_id :02d}.txt", "w",
                  encoding='utf-8') as new_file:
            new_file.write(Archivos.to_json(self))
        Hotel.create_reservation(self)

    def borrar(self):
        """Método para borrar fisicamente la información de la clase"""
        try:
            os.remove(f"{self.prefix}{self.obj_id :02d}.txt")
            Hotel.cancel_reservation(self)
        except FileNotFoundError:
            print(f"El registro de Reservación {self.obj_id} no existe")

    def load(self, obj_id):
        """Método para cargar desde archivo la información de la clase"""
        filename = f"{self.prefix}{obj_id :02d}.txt"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                reservation = Reservation.from_dict(data)
                f.close()
                return reservation
        except FileNotFoundError:
            print(f"Reservación {obj_id} no encontrada, no se pudo cargar")
            return None

    def get_next_id(self):
        """Método para establecer el siguiente id de hotel"""
        return Archivos.get_next_id_from_file("R")

    def imprimir_detalle(self):
        """Método para imprimir la información de Reservación"""
        print(f"Reservación '{self.customer_id}' - {self.hotel_id}")

    @classmethod
    def from_dict(cls, dt):
        """Método para crear un objeto desde un diccionario"""
        return cls(dt['obj_id'], dt['customer_id'], dt['hotel_id'],
                   dt['room'])

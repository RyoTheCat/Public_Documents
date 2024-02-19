"""
Ejemplo de pruebas unitarias
"""
import unittest
from hotel import Hotel


class TestHotelMethods(unittest.TestCase):
    """Clase de pruebas"""

    numbers = []

    def setUp(self):
        """Prueba unitaria - SetUp"""
        for i in range(0, 2):
            self.hotel = Hotel(-1, f"Prueba{i}",
                                   f"Location {i}", 50)
            self.hotel.guardar()
            self.numbers.append(self.hotel.obj_id)

    def tearDown(self):
        """Prueba unitaria - Teardown"""
        for i, _resort_name in enumerate(self.numbers):
            obj_id = self.numbers[i]
            self.hotel = self.hotel.load(obj_id)
            self.hotel.borrar()
        print("Limpiando información de Hoteles")
        self.numbers.clear()
        print("\n")

    def test_save(self):
        """Prueba unitaria - Método Guardar"""
        self.hotel.guardar()

    def test_delete(self):
        """Prueba unitaria - Método Borrar"""
        obj_id = self.numbers[0]
        self.hotel = self.hotel.load(obj_id)
        self.hotel.borrar()
        print(f"Intentando borrar el Hotel {self.hotel.obj_id}")
        self.numbers.remove(obj_id)

    def test_not_delete_error(self):
        """Prueba unitaria - Método Borrar - Error"""
        obj_id = self.numbers[0]
        self.hotel = self.hotel.load(obj_id)
        self.hotel.obj_id = 99999
        self.hotel.borrar()

    def test_print(self):
        """Prueba unitaria - Método Imprimir información"""
        print("Desplegando información de hoteles")
        self.hotel.imprimir_detalle()

    def test_not_load(self):
        """Prueba unitaria Negativa - Método cargar información"""
        self.hotel.load(9999)

    def test_modify(self):
        """Prueba unitaria - Método Modificar información"""
        print("Modificando información de hoteles")
        obj_id = self.numbers[1]
        self.hotel = self.hotel.load(obj_id)
        print("Antes de modificar")
        self.hotel.imprimir_detalle()
        self.hotel.resort_name = "Prueba de modificación"
        print("Después de modificar")
        self.hotel.imprimir_detalle()

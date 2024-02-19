"""
Ejemplo de pruebas unitarias
"""
import unittest
from datetime import date
from customer import Customer


class TestCustomerMethods(unittest.TestCase):
    """Definición de la clase de pruebas unitarias para Customer"""

    numbers = []

    def setUp(self):
        """Prueba unitaria - SetUp"""
        for i in range(0, 2):
            self.customer = Customer(-1, f"Nombre {i}",
                                         f"Apellido {i}",
                                         date(2000+i, 3+i, 10+i)
                                         .strftime("%d/%m/%Y"))
            self.customer.guardar()
            self.numbers.append(self.customer.obj_id)

    def tearDown(self):
        """Prueba unitaria - Teardown"""
        for i, _resort_name in enumerate(self.numbers):
            obj_id = self.numbers[i]
            self.customer = self.customer.load(obj_id)
            self.customer.borrar()
        print("Limpiando información de Clientes")
        self.numbers.clear()
        print("\n")

    def test_save(self):
        """Prueba unitaria - Método Guardar"""
        self.customer.guardar()

    def test_delete(self):
        """Prueba unitaria - Método Borrar"""
        obj_id = self.numbers[0]
        self.customer = self.customer.load(obj_id)
        self.customer.borrar()
        print(f"Intentando borrar el Cliente {self.customer.obj_id}")
        self.numbers.remove(obj_id)

    def test_not_delete_error(self):
        """Prueba unitaria - Método Borrar - Error"""
        obj_id = self.numbers[0]
        self.customer = self.customer.load(obj_id)
        self.customer.obj_id = 99999
        self.customer.borrar()

    def test_print(self):
        """Prueba unitaria - Método Imprimir información"""
        self.customer.imprimir_detalle()

    def test_not_load(self):
        """Prueba unitaria Negativa - Método cargar información"""
        self.customer.load(9999)

    def test_modify(self):
        """Prueba unitaria - Método Modificar información"""
        obj_id = self.numbers[1]
        self.customer = self.customer.load(obj_id)
        print("Antes de modificar")
        self.customer.imprimir_detalle()
        self.customer.first_name = "Nuevo nombre"
        print("Después de modificar")
        self.customer.imprimir_detalle()

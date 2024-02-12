"""Materia: Pruebas de software y aseguramiento de la calidad.
# Tarea: 5.2 Ejercicio de programación 1 - Compute Sales.
# Autor: Héctor Raúl Vázquez González - A00565542.
"""
import sys
import json

# Reading file name from parameters
Catalog_file = sys.argv[1]
Sales_file = sys.argv[2]
WRITE_FILE = "SalesResults.txt"
Sales_list = []
Product_list = []


class Product:
    def __init__(self, name, price, quantity):
        self.title = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


class Sale:
    def __init__(self, sale_id, date):
        self.id = sale_id
        self.date = date
        self.PRODUCTS = []

    def total(self):
        if len(self.PRODUCTS) <= 0:
            return 0
        else:
            sales = 0
            for item in self.PRODUCTS:
                sales = sales + item.total()
            return sales


def readfile(path):
    with open(path) as file:
        file_contents = file.read()
    return file_contents


def parse_catalog(cat):
    lista = []
    for item in cat:
        lista.append(Product(item["title"], item["price"], 0))
    return lista


def existe_en_lista(sale_id, lista):
    for item in lista:
        if item == sale_id:
            return True
    return False


def get_SalesID(lista_sales):
    lista_ids = []
    for item in lista_sales:
        if not existe_en_lista(item["SALE_ID"], lista_ids):
            lista_ids.append(item["SALE_ID"])
    return lista_ids


def get_price(name,  catalog):
    for item in catalog:
        if item["title"] == name:
            return item["price"]
    return 0


def get_salesBy_id(sale_id, lista_ventas, catalog):
    lista_resultado = []
    primero = True
    date = ""
    for item in lista_ventas:
        if item["SALE_ID"] == sale_id:
            if primero:
                date = item["SALE_Date"]
                primero = False
            lista_resultado.append(Product(item["Product"],
                                   get_price(item["Product"], catalog),
                                   item["Quantity"]))
    venta = Sale(sale_id, date)
    venta.PRODUCTS = lista_resultado.copy()
    return venta


def parse_ventas(lista_ids,  lista_ventas, catalogo):
    lista_de_Ventas = []
    for item_id in lista_ids:
        lista_de_Ventas.append(get_salesBy_id(item_id, lista_ventas, catalogo))
    return lista_de_Ventas


def print_Sales(sales_list):
    for item in sales_list:

        print("*****  Id: " + str(item.id) +
              " Date: " + str(item.date) + "******")
        iterator = 1
        for p in item.PRODUCTS:
            print(str(iterator) + "-> " + str(p.title) + "------")
            print("--- Quantity: " + str(p.quantity) +
                  " total: " + str(p.total()))
            iterator = iterator + 1
        print("*** Total: " + str(float(item.total())) + "***")


def save_sales(sales_list):
    lines = []
    grand_total = 0
    for item in sales_list:

        lines.append("*****  Id: " + str(item.id) +
                     " Date: " + str(item.date) + "******\n")
        iterator = 1
        for p in item.PRODUCTS:
            lines.append(str(iterator) + "-> " +
                         str(p.title) + "------\n")
            lines.append("--- Quantity: " + str(p.quantity) +
                         " total: " + str(p.total()) + "\n")
            iterator = iterator + 1
        lines.append("*** Total: " + str(float(item.total())) + "***\n")
        
        grand_total = grand_total + float(item.total())
    lines.append("*** " + Sales_file + " Grand Total: " +
                 str(grand_total) + "***\n")
    f = open(WRITE_FILE, "a")
    f.writelines(lines)
    f.close()


def main():
    """Principal function"""

    """Se carga los datos de los productos"""
    catalog = json.loads(readfile(Catalog_file))

    "Se carga la lista de ventas"
    Sales = json.loads(readfile(Sales_file))

    "Se carga La lista de Ids"
    Ids_de_Ventas = get_SalesID(Sales)

    "Se carga la lista de Ventas"
    sales_made_list = parse_ventas(Ids_de_Ventas, Sales, catalog)

    print_Sales(sales_made_list)
    save_sales(sales_made_list)


print(main())

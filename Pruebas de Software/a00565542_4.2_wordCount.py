"""Materia: Pruebas de software y aseguramiento de la calidad.

Tarea: 4.2 Ejercicio de programación 3 - Count Words.

Autor: Héctor Raúl Vázquez González - A00565542.
"""

import sys
import time

# Reading file name from parameters
FILE_NAME = sys.argv[1]
WRITE_FILE = "WordCountResults.txt"

# Functions of the program for statistical calculations
def read_file():
    """Read a file."""
    with open("P3/" + FILE_NAME, mode='r', encoding='utf-8') as file:
        data = file.readlines()
        file.close()
        return data

def write_document(data):
    """Create a file."""
    with open("P3/" + WRITE_FILE, mode='a', encoding='utf-8') as file:
        file.write(data)
        file.close()

def main():
    """Principal function to count words"""
    list_ = []
    elements = 0
    info = ""

    words_list = read_file()    # Reading yhe file

    # Counting words algorithm
    for word in words_list:
        word = word.strip().upper()

        if word.isalpha():

            bandera = False
            for line in list_:
                if line["word"] == word:
                    bandera = True
                    line["number"] += 1

            if not bandera:
                list_.append({"word": word, "number": 1})

        else:
            info += f"\nInvalid element: {line}."

        elements += 1

    # Reading the results and putting them in a string
    for item in list_:
        info += "\n" + item["word"] + " " + str(item["number"])

    time_ = time.time()    # Measuring the time it takes to execute

    info += f"\nTotal of results: {elements}"
    info += f"\nTime of execution: {time_}"

    write_document(info)    # Writing the results in a file

print(main())

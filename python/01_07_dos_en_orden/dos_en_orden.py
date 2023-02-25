'''
Programa: 01_07_dos_en_orden
Toma 2 valores enteros, ordena la salida de estos numeros de menor a mayor.

__author__ = "Alvaro Juanez Mamani"
__version__ = "1.0"
__email__ = "alvarojuanezgit01@gmail.com"
__status__ = "Aprendiendo python"
'''

num_1 = int(input("Primer numero? "))
num_2 = int(input("Segundo  numero? "))

#Ordena los numero de menor a mayor
if num_1 > num_2:
    print(num_2, " i ", num_1)
else:
    print(num_1, " i ", num_2)

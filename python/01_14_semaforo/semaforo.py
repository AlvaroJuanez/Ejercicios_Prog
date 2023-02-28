'''
Programa 01_14_semaforo
El programa simula el funcionamiento de un semafor al cual le daremos colores y el respondera en
función a ellos.

__author__ = "Alvaro Juanez M"
__version__ = "1.0" 27/02/2023
__status__ = "Aprendiendo python"

'''
# Obten los datos
color = str(input("Color? "))

# Condiciona los resultado en función al color
if color == "Rojo" or color == "rojo":
    print("Alto!! ")
elif color == "Amarillo" or color == "amarillo":
    print("Detente aun no!! ")
elif color == "Verde" or color == "verde":
    print("Ya puedes pasar")

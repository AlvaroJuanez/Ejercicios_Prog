'''
Programa : 01_04_nombre_y_apellidos.py
El siguiente programa toma 2 valores Strings por consola, para entablar un pequeña charla donde
obtendremos el nombre y apellido del usuario.

__author__ = "Alvaro Juanez Mamani"
__version__ = "1.0"
__email__ = "alvarojuanezgit01@gmail.com"
__status_ = "Aprendiendo Python"
'''

NOMBRE = str(input("Como te llamas? "))
APELLIDO = str(input("Y cual es tu primer apellido? "))     #Nombre de los Strings en Mayusculas

print("Oye ", NOMBRE, " tengo un amigo que tambien es ", APELLIDO + ".")

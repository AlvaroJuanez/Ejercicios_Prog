'''
Programa : 01_03_horas_trabajadas.py
El programa pide al usuario 2 numero enteros positivos, el primer numero indica cuantas horas
trabajo en una jornada.
El segundo numero es el precio que cobra el trabajador por hora, con ambos datos nos dara la
media y el monto que se gano e la jornada laboral.

__author__ = "Alvaro Juanez Mamami"
__version__ = "1.0"
__email__ = "alvarojuanezgit01@gmail.com"
__status__ = "Aprendiendo Python"
'''

horas = int(input("Cuantas horas trabajaste hoy?  "))   # Toma un valor entero
valor = int(input("Precio de la hora en Bs  "))

total = horas * valor
print("El total ganado el dia de hoy es ", total)   #Imprime el valor total ganado

'''
Programa : 01_15_numero_de_hijos
Este programa te pregunta la cantidad de hijos que tienes, y te respondera acorde al numero,
Las respuestas pueden ser graciosas o no.

__author__ = "Alvaro Juanez Mamani"
__version__ = "1.0" 8/03/2023
__status__ = "Aprendiendo python"
'''

#Obtén los datos necesarios
hijos = int(input("Cuantos hijos tienes? "))

#Acorde al numero de hijos responde
if hijos < 0:
    print("No puedes tener menos de 0 hijos! ")
elif hijos == 0:
    print("Mira todo lo que te ahorras en pañales ")
elif hijos == 1:
    print("Trata de no mimarlo mucho ")
elif hijos >= 1 and hijos <= 5:
    print("No te aburres en casa ")
elif hijos > 4:
    print("Tu si haces pais ")

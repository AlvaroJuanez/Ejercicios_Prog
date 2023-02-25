'''
Programa: 01_06_la_prisión
Programa en función a la edad. Determina si eres mayor de edad, y si puedes ir legalmente a prisión
de lo contrario imprimira un mensaje  totalmente opuesto.
Para ello haremos uso de las condionales if else.
__author__ = "Alvaro Juanez Mamani"
__version__ = "1.0"
__email__ = "alvarojuanezgit01@gmail.com"
__status__ = "Aprendiendo python"
'''

nombre = input("Como te llamas? ")
edad = int(input("Qué edad tienes? "))

#Condiciones de edad
if edad >= 18:
    print(nombre, " Eres mayor de edad, ten cuidado \npuedes ir a la carcel")
else:
    print(nombre, " Eres menor ten cuidado")

'''
Programa: 01_09_dias_de_la_semana
El programa recibe numeros entero como argumento, para cada numero se le asignara un dia por tanto
si 1 es lunes, 2 sera martes...etc
si los numeros superan al numero de días en la semana mostrara por pantalla un error.

__author__ = "Alvaro Juanez M"
__version__ = "1.0" 24-02-2023
__status__ = "Aprendiendo python"
'''
import sys #Libreria que permite acceder funciones del sistema

dia = int(sys.argv[1])  #Permite introducir un valor como argumento

#Verifica si el valor es inferior o superior al numero de días
#de ser asi muestra por pantalla error.
if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
elif dia <= 0 or dia > 7:
    print("Error")

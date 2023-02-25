'''
Programa : 01_08_pares_impares
El programa tomas 2 valores enteros, si la es divisible entre 2 o si el residuo de la división
es 0, interpreta que el numero es par caso contrario impar y lo muestra por pantalla.

__author__ = "Alvaro juanez M"
__version__ = "1.0"
__status__ = "Aprendiendo python"
'''
import sys #Modulo libreria, da acceso a funciones especificas del sistema


numero = int(sys.argv[1]) #metodo para introducir un valor como argumento por consola

#Verifica si el numero es par o impar
if numero % 2 == 0:
    print("El numero ", numero, " es par")
else:
    print("El numero ", numero, " es impar")

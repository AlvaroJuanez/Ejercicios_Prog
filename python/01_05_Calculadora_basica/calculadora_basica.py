'''
Programa: 01_05_calculadora_basica
Simula el comportamiento de una calculadora basica El usuario Introducira 2 numeros enteros,
Los cuales se procesaran para mostrar por pantalla los resultado de una suma, resta, multiplicación,
división.

__author__ = "Alvaro Juanez M"
__version__ = "1.0"
__email__ = "alvarojuanezgit01@gmail.com"
__status__ = "Aprendiendo python"
'''

num_1 = int(input("Introduce el primer numero "))
num_2 = int(input("Introduce el segundo numero "))

# Operaciones basicas
suma = num_1 + num_2
resta = num_1 - num_2
multi = num_1 * num_2
division = int(num_1 / num_2)

#Imprime los resultados
print(num_1 , " + ", num_2, " = ", suma)
print(num_1 , " - ", num_2, " = ", resta)
print(num_1 , " * ", num_2, " = ", multi)
print(num_1 , " / ", num_2, " = ", division)

'''
Programa: 01_12_calculadora_sencilla
Simula una calculadora sencilla, en su segunda versión del programa 01_05_calculadora_basica, pero
en esta versión ya  no realiza en su totalidad las operaciones y las muestra por pantalla.

El programa identifica el tipo de dato y el caracter para hacer la operación matematica, para
luego mostrar solo el resultado de los que el usuario pida.
__author__ = "Alvaro Juanez Mamani"
__version__ = "2.0" 27/02/2023
__status__ = "Aprendiendo python"
'''
# Obten los datos necesario
num_1 = float(input("Primer numero "))
operador = input("Operador ")
num_2 = float(input("Segundo numero "))

# Operaciones basicas
suma = num_1 + num_2
resta = num_1 - num_2
multi = num_1 * num_2
division = num_1 / num_2

# Opera la calculadora en funcion al operacor(caracter).
if operador == '+':
    print(num_1, str(operador), num_2, " = ", suma)
elif operador == '-':
    print(num_1, str(operador), num_2, " = ", resta)
elif operador == '*':
    print(num_1, str(operador), num_2, " = ", multi)
elif operador == '/':
    print(num_1, str(operador), num_2, " = ", division)

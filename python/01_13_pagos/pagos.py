'''
Programa: 01_13_pagos
Simula una transacción economica con la cantidad a pagar, de manera que indique si falta o sobra
dinero.
__author__ = "Alvaro Juanez M"
__version__ = "1.0"
__status__ = "Aprendiendo python"
'''

# Obten los datos necesarios
precio = int(input("Precio? "))
paga = int(input("Paga? "))

# Opera si se debe o sobra
falta = precio - paga
sobra = paga - precio

# Verifica si sobra o falta dinero
if precio > paga:
    print("Faltan ", falta, " Bs")
elif paga > precio:
    print("Sobran ", sobra, " Bs")
elif paga == precio:
    print("No se debe, ni sobra nada ")

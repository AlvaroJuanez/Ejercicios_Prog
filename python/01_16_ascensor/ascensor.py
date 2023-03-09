'''
Programa : 01_16_Ascensor
El ascensor en este programa consta de 3 plantas:
    planta baja
    primer piso
    segundo piso.

la interacción sera la misma de un ascensor pero si el usuario pide subir a un piso inexistente
tanto en la subida o bajada el programa devolvera un mensaje de  Error!.

__author__ = "Alvaro Juanez Mamani"
__version__ = "1.0" 9/04/2023
__status__ = "Aprendiendo python"
'''

#Obten los datos necesarios para el programa
PISO = str(input("Piso? "))
BOTON = str(input("Boton? "))

#Condiciona es uso del ascensor acorde a los pisos disponibles
if PISO == "planta baja":   #Planta baja
    if BOTON == "subir uno":
        print("primer piso")
    elif BOTON == "subir dos":
        print("segundo piso")
    else:
        print("Error!")
elif PISO == "primer piso":     #Primer piso
    if BOTON == "subir uno":
        print("segundo piso")
    elif BOTON == "bajar uno":
        print("planta baja")
    else:
        print("Error!")
elif PISO == "segundo piso":    #Segundo piso
    if BOTON == "bajar dos":
        print("planta baja")
    elif PISO == "bajar uno":
        print("primer piso")
    else:
        print("Error!")

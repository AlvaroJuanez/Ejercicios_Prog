'''
Programa: 01_10_meses_y_años
El programa toma 2 valores enteros, mes y año posteriormente el resultado del mismo mostrara
por pantalla una fecha anterior y posterior tanto del mes y el años de los datos que introduzcamos

__author__ = "Alvaro Juanez M"
__version__ = "1.0" 26-02-2023
__status__ = "Aprendiendo python"
'''
#obten los valores requeridos para el programa
mes = int(input("Mes? "))
year = int(input("Año? "))

#Opera meses y años posterior
posterior = mes + 1
year_posterior = year + 1

#Opera meses y años anterior
anterior = mes - 1
year_anterior = year - 1

#Si el mes es mayor a 1 y menor de 12
if mes > 1 and mes < 12:
    print("Anterior ", anterior, "/", year, " i ", "Posterior ", posterior, "/", year)
    #si el mes es 12
elif mes == 12:
    print("Anterior ", anterior, "/", year, " i ", "Posterior ", mes - 11, "/", year_posterior)
    #si el mes es 1
elif mes == 1:
    print("Anterior ", mes + 11, "/", year_anterior, " i ", "posterior ", posterior, "/", year)

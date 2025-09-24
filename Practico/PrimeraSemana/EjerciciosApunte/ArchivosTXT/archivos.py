"""
Desarrollar un programa que lea todo el contenido del archivo numeros.txt que contiene múltiples líneas de texto, cada una de ellas con un número entero. Al leer el archivo se debe almacenar todos los números en una lista. A continuación, el programa debe manipular los números cargados en la lista para

Calcular e imprimir el promedio de todos los numeros
Calcular e imprimir la cantidad de numeros mayores al promedio
Generar y mostrar una nueva lista que contenga tods los pares
"""

import os

def leerArchivo(nombre):
    try:
        with open(nombre, "r") as f:
            contenido = [int(linea.strip()) for linea in f.readlines()]
            return contenido
    except FileNotFoundError:
        #Archivo no encontrado
        print("Error al encontrar el archivo")
    except IOError:
        #Otro error
        print("Error")



def calcular_promedio(contenido):
    suma_total = 0
    cant_numeros = len(contenido)
    for linea in contenido:
        suma_total += linea
    
    return suma_total / cant_numeros
"""
def calcular_promedio_10(contenido):
    suma_total = 0
    cant_numeros = 10
    cont = 1
    for linea in contenido:
        if cont <= 10:
            #print(f"linea: {linea}")
            numero = int(linea.strip())
            print(f"numero: {numero}")
            suma_total += numero
            cont += 1

    return suma_total / cant_numeros
"""

def cant_mayor_prom(contenido, promedio):
    cont_mayores_prom = 0

    for linea in contenido:
        if(linea > promedio):
            cont_mayores_prom += 1
    
    return cont_mayores_prom

def lista_pares(contenido):
    nueva_lista = []

    for linea in contenido:
        if (linea%2==0):
            nueva_lista.append(linea)
    
    return nueva_lista



if __name__ == "__main__":
    print("*"*20)
    base_dir = os.path.dirname(__file__) # Obtener directorio actual
    
    archivo = os.path.join(base_dir, "numeros.txt") #Obtener ruta completa
    
    contenido = leerArchivo(archivo)

    #Mostrar contenido
    """
    for linea in contenido:
        numero = linea.strip()

        print(numero)
    """
    
    #Mostrar Resultads
    print(f"{"*"*20} Resultados {"*"*20}")

    promedio = calcular_promedio(contenido)
    print(f"Promedio de todos los numeros: {promedio}")

    cant_mayor_promedio = cant_mayor_prom(contenido, promedio)

    print(f"Cantidad de numeros mayores a {promedio} es {cant_mayor_promedio}")
    
    listar_pares = lista_pares(contenido)

    print(f"{"*"*20} Contiene {len(listar_pares)} numeros pares, y son: {"*"*20}")

    for par in listar_pares:
        print(par) 
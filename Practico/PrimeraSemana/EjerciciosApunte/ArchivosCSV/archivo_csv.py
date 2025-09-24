import os

def leer_archivo(nombre):
    lista_provincias = []
    try:
        with open(nombre, 'r') as f:
            linea = f.readline()
            while(linea):
                linea_separada = linea.strip().split(";")
                #print(type(linea_separada))
                print(linea_separada) #Lista de los componentes
                #Construir el diccionario
                provincia = construir_dict(linea_separada)
                print(provincia)
                linea = f.readline()
                lista_provincias.append(linea)
            return lista_provincias
    except FileNotFoundError:
        print("Error al encontrar el archivo")

def construir_dict(lista_valores):
    provincia_dict = {
        'Provincia': None,
        'Codigo' : None,
        'Nombre' : None
    }
    for i in range(len(lista_valores)):
        for x in range(len(list((provincia_dict.keys())))):
            if x == i:
                list(provincia_dict.values())[i] = lista_valores[i]
    

    return provincia_dict
                




if __name__ == "__main__":

    dir = os.path.dirname(__file__)

    archivo = os.path.join(dir,"cp.csv")

    contenido = leer_archivo(archivo)

    #print(contenido)
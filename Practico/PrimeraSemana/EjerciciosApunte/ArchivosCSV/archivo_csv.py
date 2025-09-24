import os

def leer_archivo(nombre):
    lista_provincias = []
    try:
        with open(nombre, 'r') as f:
            linea = f.readline()
            while(linea):
                linea_separada = linea.strip()
                print(linea_separada)
                f.readline()
            return contenido
    except FileNotFoundError:
        print("Error al encontrar el archivo")





if __name__ == "__main__":

    dir = os.path.dirname(__file__)

    archivo = os.path.join(dir,"cp.csv")

    contenido = leer_archivo(archivo)

    #print(contenido)
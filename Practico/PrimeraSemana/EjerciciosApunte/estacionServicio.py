print("*"*10+"Estacion De Servicio"+"*"*10)

def cargar_surtidores(n):
    estacion_servicio = []
    TIPOS = {1: "Nafta", 2: "Nafta Especial", 3: "Gasoil"}


    for i in range(n):
        
        numeroSurtidor = int(input("Ingrese el numero del surtidor: "))
        while( not( 1<=numeroSurtidor<=30 ) ):
            numeroSurtidor = int(input("Ingrese el numero del surtidor[1-30]: "))

        litrosVendidos = int(input("Ingrese la cantidad de litros vendidos del surtidor: "))
        while(not (litrosVendidos > 0) ):
            litrosVendidos = int(input("Ingrese la cantidad de litros vendidos del surtidor: ", numeroSurtidor))
        print(
            "Tipo de nafta:\n"
            "1 -> Nafta\n"
            "2 -> Nafta Especial\n"
            "3 -> Gasoil"
        )
        tipoNafta = int(input("Ingrese el tipo [1-3]: "))
        while not (1 <= tipoNafta <= 3):
            tipoNafta = int(input("Ingrese el tipo [1-3]: "))

        registro = {
            "Nro Surtidor": numeroSurtidor,
            "Litros vendidos": litrosVendidos,
            "Tipo de Nafta Vendida": TIPOS[tipoNafta],
        }
        estacion_servicio.append(registro)

    
    return estacion_servicio #Lista de diccionarios


def calc_total_combustible(registros):
    total_nafta = 0
    total_nafta_especial = 0
    total_gasoil = 0
    
    for r in registros:
        if r["Tipo de Nafta Vendida"] == "Nafta":
            total_nafta += r["Litros vendidos"]
        elif r["Tipo de Nafta Vendida"] == "Nafta Especial":
            total_nafta_especial += r["Litros vendidos"]
        elif r["Tipo de Nafta Vendida"] == "Gasoil":
            total_gasoil += r["Litros vendidos"]

    return total_nafta, total_nafta_especial, total_gasoil

def buscar_minimo_venta(registros):
    if not registros:
        return None
    
    minimo = registros[0]

    for i in registros[1:]:
        if i["Litros vendidos"] < minimo["Litros vendidos"]:
            minimo = i
    

    return minimo["Nro Surtidor"]


if __name__ == '__main__':
    estacion_servicio = cargar_surtidores(2)  # Lista de diccionarios

    for i in (estacion_servicio):
        #Itero el diccionario
        for k,v in i.items():
            print(f"{k}:{v}")
        print("*"*20)
    

    #Lista de surtidores
    print("*"*20, 'Lista de surtidores', "*"*20)
    print(estacion_servicio)

    print("*"*20, "Primer Punto", "*"*20)
    total_nafta, total_nafta_especial, total_gasoil = calc_total_combustible(estacion_servicio)

    print("Total de nafta vendida: ", total_nafta)
    print("Total de nafta especial vendida: ", total_nafta_especial)
    print("Total de gasoil vendido: ", total_gasoil)   

    print("*"*20, "Segundo Punto", "*"*20)

    minimo = buscar_minimo_venta(estacion_servicio)

    print("Numero de surtidor que vendio menos combustible: ", minimo )

    #Promedio de nafta vendida general
    suma_total = total_nafta + total_nafta_especial + total_gasoil
    promedio = suma_total / len(estacion_servicio)

    print("El promedio por surtidor es de: ", promedio , "litros")
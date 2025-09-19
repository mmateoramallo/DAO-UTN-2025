def validar_rango(minimo, maximo):
    valor = float(input("Ingrese un valor: "))
    while(not(minimo <= valor <= maximo)):
        print(f"Ingrese un valor entre los rangos definidos minimo: {minimo} | maximo: {maximo}")
        valor = float(input("Ingrese un valor: "))
    
    return valor

def cargar_termperaturas():
    temperaturas = []
    
    valor = validar_rango(-20, 50)
    while(valor != 50):
        temperaturas.append(valor)
        valor = validar_rango(-20, 50)

    return temperaturas
        

def cant_bajo_cero(temperaturas):

    cant_dias = 0 
    for t in temperaturas:
        if t < 0:
            cant_dias += 1
    
    return cant_dias

def calc_promedio(temperaturas):

    cant_dias = len(temperaturas)
    temp_total = 0
    for t in temperaturas:
        temp_total += t
    
    return temp_total / cant_dias

def calc_promedio_calidos(temperaturas):
    calidos = [t for t in temperaturas if t > 20]
    if not calidos:
        return None
    return sum(calidos) / len(calidos)

def mayor_40(temperaturas):
    for t in temperaturas:
        if t > 40:
            return "Si"
            break
    
    return "No"

def mayor_no_calidos(temperaturas):

    no_calidos = [t for t in temperaturas if t <= 20]
    if not no_calidos:
        return None
    return max(no_calidos)

def cant_menor_prom(temperaturas, promedio):
    cant_dias = 0
    for t in temperaturas:
        if t < promedio:
            cant_dias += 1

    return cant_dias

if __name__ == "__main__":

    temperaturas = cargar_termperaturas()
    
    for i in temperaturas:
        print(i)

    #PrimerPunto
    dias_bajo_cero = cant_bajo_cero(temperaturas)

    #SegundoPunto
    temp_promedio = calc_promedio(temperaturas)

    #Promedio de temperatura de dias calidos > 20
    temp_dias_calidos = calc_promedio_calidos(temperaturas)

    #Mostrara si o no si hubo un dia con T > 40
    hubo_mas_40 = mayor_40(temperaturas)

    #Mayor Teperaturas de los dias que no fueron calidos < 20
    mayor = mayor_no_calidos(temperaturas)

    #Cantidad de dias con temperatura menor al promedio
    cant_dias = cant_menor_prom(temperaturas, temp_promedio)


    print("\nResultados")
    print(f"- Cantidad de días bajo cero: {dias_bajo_cero}")
    print(f"- Promedio de temperaturas: {temp_promedio if temp_promedio is not None else 's/datos'}")
    print(f"- Promedio de días cálidos (>20): {temp_dias_calidos if temp_dias_calidos is not None else 'no hubo días >20'}")
    print(f"- ¿Hubo algún día con más de 40°?: {hubo_mas_40}")
    print(f"- Mayor temperatura de los días no cálidos (≤20): {mayor if mayor is not None else 'no hubo'}")
    print(f"- Cantidad de días con temperatura menor al promedio: {cant_dias}")

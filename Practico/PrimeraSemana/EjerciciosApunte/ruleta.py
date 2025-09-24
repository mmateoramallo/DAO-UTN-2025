"""
Desarrollar un programa que simule el juego de la ruleta.

Para ello generar al azar 1000 tiradas y luego informar:

Cantidad de pares e impares
Cantidad de tiradas por cada docena
Porcentaje de ceros sobre el total de jugadas.
Cantidad de rojos y de negros


10 Y 28 = > Negros
Sumar digitos de cada numero es par => Negro (Si el numero es mayor a 9 no es valido, debe ser un unico digito)


"""
import random

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

def get_color(nro):
    if nro == 0:
        return 'V'
    elif nro == 10 or nro == 28:
        return 'N'
    else:
        if reducir_nro(nro)%2==0:
            return 'N'
        else:
            return 'R'

def reducir_nro(nro):
    if nro < 10:
        return nro
    else:
        digitos = [int(digito) for digito in str(nro)]
        #print(digitos)
        suma = sum(digitos)
        #print(suma)
        return reducir_nro(suma)

def generar_ruleta():
    ruleta = []
    for nro in range(0,37):
        ruleta.append((nro, get_color(nro)))

    return ruleta

def imprimir_ruleta(rul: list[(int,str)]):
    # Primero creas una instancia (un objeto) de la clase Console
    console = Console() 
    col = 1
    for nro,color in rul:
        if color == 'V':
            console.print (f"[bold white on green]{nro:^12}[/]", end="")
            print()
        elif color == 'R':
            console.print (f"[bold white on red]{nro:^4}[/]", end="")
            col += 1
        else:
            console.print (f"[bold white on black]{nro:^4}[/]", end="")
            col += 1
        
        if col == 4:
            print()
            col = 1

def imprimir_tirada (nro : int, color : str):
    console = Console() 
    if color == 'V':
        console.print (f"Obtuvimos [bold white on green]{nro}{color}[/]")
    elif color == 'R':
        console.print (f"Obtuvimos [bold white on red]{nro}{color}[/]")
    else:
        console.print (f"Obtuvimos [bold white on black]{nro}{color}[/]")

def determinar_docena(nro):
    print(nro)
    if (1 <= nro <= 12):
        return 1
    elif(13 <= nro <= 24):
        return 2
    elif (25 <= nro <= 36):
        return 3


def simulacion(ruleta):
    cant_pares = cant_impar = 0
    docenas = [0,0,0]
    colores = {"V": 0, "R": 0, "N": 0}
    jugadas = 1000

    for i in range(jugadas):
        numero = random.randint(0,36)
        tirada_color = ruleta[numero][1]

        if numero%2==0:
            cant_pares += 1
        else:
            cant_impar += 1

        #Determinar docena
        docenas[determinar_docena(numero) -1] +=1

        #Sumar cantidades 
        #V = 0
        #R = 1
        #N = 2
        colores[tirada_color] +=1

    #Porcentaje de ceros
    porc_ceros = colores["V"] * 100 / jugadas
    console = Console()
    table = Table(title="Resultados de la simulación")
    table.add_column("Resultado")
    table.add_column("Valor", justify="center")

    table.add_row("Cantidad de pares", str(cant_pares))
    table.add_row("Cantidad de impares", str(cant_impar))
    table.add_row("Cantidad de tiradas 1º docena", str(docenas[0]))
    table.add_row("Cantidad de tiradas 2º docena", str(docenas[1]))
    table.add_row("Cantidad de tiradas 3º docena", str(docenas[2]))
    table.add_row("Porcentaje de ceros", f"{porc_ceros:.2f}%")
    table.add_row("Cantidad de rojos", f"[bold white on red]{colores['R']}[/]")
    table.add_row("Cantidad de negros", f"[bold white on black]{colores['N']}[/]")



if __name__ == "__main__":
    ruleta = generar_ruleta() #Definimos el tablero
    imprimir_ruleta(ruleta)
    simulacion(ruleta)
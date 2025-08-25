"""  
Crea un programa que:

Pida al usuario que ingrese productos y precios hasta que escriba "fin".

Guarde todo en una lista de tuplas ([(producto, precio), ...]).

Al final, muestre el total a pagar y el producto más caro.

👉 Practicás: listas, bucles, condicionales.
"""


def solicitarProductos():
    productos = []
    
    productoCarga = input('Ingrese el nombre de un producto a cargar: ')
    precioProductos = float(input('Ingrese el precio del producto a cargar: '))
    if(not(productoCarga == 'fin')):

        productoIngresado = (productoCarga, precioProductos)
        productos.append(productoIngresado)

    while(productoCarga != 'fin'):
        productoCarga = input('Ingrese el nombre de un producto a cargar: ')
        if(productoCarga == 'fin'):
            break
        else:
            precioProductos = float(input('Ingrese el precio del producto a cargar: '))
            productoIngresado = (productoCarga, precioProductos)
            productos.append(productoIngresado)


    return productos



if __name__ == '__main__':
    productos = solicitarProductos()
    #Sumar valor de cada uno
    total = 0
    mayorPrecio = None
    for p in productos:
        total += p[1]
        mayorPrecio = p
        
        if(p[1] > mayorPrecio[1]):
            mayorPrecio = p
    print(productos)

    print('La suma del total de los productos es de: ', total, '$')
    print('El precio del producto de mayor valor es: ', mayorPrecio[1], '| Producto: ', mayorPrecio)
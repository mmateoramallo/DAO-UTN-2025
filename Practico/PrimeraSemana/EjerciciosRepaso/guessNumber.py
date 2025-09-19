import random

def generarAleatorio():
    return random.randrange(1,100);

if __name__ == '__main__':
    numero = generarAleatorio()
    
    print('Numero Aleatorio Generado!!')

    numeroUsuario = int(input('Ingresa el numero que crees que es en el rango de (1,100): '))

    while(numeroUsuario != numero):
        print('Numero sin adivinar! ')
        if(numeroUsuario > numero):
            print('Frio Frio Frioooo, para abajo...')
        elif(numeroUsuario < numero):
            print('Frio Frio Frioooo, para arriba...')

        
        numeroUsuario = int(input('Ingresa el numero que crees que es en el rango de (1,100): '))



    print('ADIVINASTE EL NUMERO')
    print('Numero generado: ', str(numero))
    print('Numero ingresado: ' ,str(numeroUsuario))
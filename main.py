from ColaEncadenada import ColaEncadenada
import random

if __name__ == "__main__":
    unaCola = ColaEncadenada()
    tiempoEsperaMaximo = 0

    tiempoSimulacion = int(input("Ingrese el tiempo de simulacion: "))

    ocupado = 0

    for i in range(tiempoSimulacion):
        if random.randrange(0, 2) == 0:
            unaCola.insertar(i)
        
        if ocupado == 0:
            if not unaCola.vacia():
                cliente = unaCola.suprimir()
                espera = i - cliente
                if espera > tiempoEsperaMaximo:
                    tiempoEsperaMaximo = espera
                ocupado = 5
        else:
            ocupado -= 1
    
    print("El tiempo promedio de espera de los clientes en la cola fue de {0:.2f} minutos".format(tiempoEsperaMaximo))
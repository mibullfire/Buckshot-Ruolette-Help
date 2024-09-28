# Probando cosas
from colorama import init, Fore, Back, Style

def pregunta(texto, opciones = "x"):
    pasar = False
    while pasar != True:
        respuesta = input(texto)
        if opciones != "x":
            if respuesta in opciones:
                pasar = True
            else:
                print(respuesta + " no es una opción válida.\n")
        else:
            if respuesta:
                pasar = True
    return respuesta

def ruleta():
    balas = pregunta("Balas Rojas / Balas Negras (R/N): ")
    pumpum = balas.split(" ")
    rojas = int(pumpum[0])
    negras = int(pumpum[1])
    total = rojas + negras
    lista = []
    for i in range (0, total):
        lista.append("x")
    fin = False
    while fin != True:
        print("La lista de Balas actual es ", lista)
        total = rojas + negras
        telefono = pregunta("Teléfono S/N: ", ["S", "N"])
        if telefono == "S":
            posicionN = pregunta("Posicion RN/x: ") # Puedo meterlo un opciones si lo divido en dos preguntas, facilitando el progreso
            bala, posicion = posicionN.split(" ")
            lista[int(posicion)-1] = bala
            if bala == "R":
                rojas -= 1
            if bala == "N":
                negras -= 1
            total -= 1
            print("Ahora la lista de balas es: ", lista)
    
        if lista[0] == "R":
            print(Fore.RED+"La probabilidad de morir es del 100%."+Fore.RESET)
        if lista[0] == "N":
            print(Fore.GREEN+"La probabilidad de morir es del 0%."+Fore.RESET)
        if lista[0] == "x":
            if rojas/total*100 >= 50:
                print(Fore.RED+"La probabilidad de morir es del ", rojas/total*100, "%."+Fore.RESET)
            else:
                print(Fore.GREEN+"La probabilidad de morir es del ", rojas/total*100, "%."+Fore.RESET)
            disparo = pregunta("¿Qué bala se ha disparado? R/N: ", ["R", "N"])
            if disparo == "R":
                rojas -= 1
            if disparo == "N":
                negras -= 1
        if lista == []:
            fin = True
        else:
            finalizar = pregunta("¿Ha terminado la parida? S/N: ", ["S", "N"])
            if finalizar == "S":
                fin = True
        lista.pop(0)
    print("Se ha finalizado el programa gracias por jugar! ")

        



ruleta()

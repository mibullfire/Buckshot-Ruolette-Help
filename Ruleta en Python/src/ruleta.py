def ruleta():

    relacion = input('Rojas/Negras')
    rojas, negras = relacion.split(' ')
    rojas, negras = int(rojas), int(negras)
    total = rojas + negras

    lista = []
    for i in range (0, total):
        lista.append('x')
    
        
    print(lista)

    muerte = False

    while total !=0 and muerte == False:
        telefono = input('Telefono S/N ')
        if telefono == 'S' or telefono == 's':
            info = input('Telefono: RN/P ')
            color, posicion = info.split(' ')
            lista[int(posicion)-1] = color
            total -= 1
            if color == 'R':
                rojas -= 1
            if color == 'N':
                negras -= 1


        print(lista)
        if lista[0] == 'x':

            print(f'Probabilidad de muerte: {round(rojas/total * 100, 1)}')
            bala = input('R/N ')
            if bala == 'R' or bala == 'r':
                rojas -= 1
            if bala =='N' or bala == 'n':
                negras -= 1 
            total = rojas + negras
        
        if lista[0] == 'N':
            print('Probabilidad de muerte: 0')
        
        if lista[0] == 'R':
            print('Probabilidad de mueerte: 100')


        lista.pop(0)
    
        fin = input('Fin S/N')
        if fin == 'S' or fin == 's':
            muerte = True

ruleta()
#función iterativa y re cursiva que calcule la suma de los cuadrados de los elementos de una lista


#iterativa
def suma(lista):
    




#  recursiva
def suma_recursiva(lista):
    if len(lista)==0:
        return 0
    
    else:
        return 2**lista[0]+suma_recursiva(lista[1:])
    
    
    
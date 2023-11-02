#modifique el algoritmo de burbuja para que pare en la primera iteración que no haga nada
#enunciado
# def bublesort(A):
#    for i in range(1, len(A)):
#        for j in range(0, len(A)-i):
#            if A[j+1] < A[j]:
#               aux= A[j]
#               A[j]=A[j+1]
#               A[j+1]=aux
# return A

#modificado
def bublesort(A):
    for i in range(1, len(A)):
        for j in range(0, len(A)-i):
            if A[j+1] < A[j]:
                #cambio
                A[j+1], A[j]= A[j], A[j+1]
                intercambio=True
            if not intercambio:
                break
    return A
        
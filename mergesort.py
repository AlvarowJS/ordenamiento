def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right[0])
            right.pop(0)
        else:
            result.append(left[0])
            left.pop(0)
    while len(left) > 0:
        result.append(left[0])
        left.pop(0)

    while len(right) > 0:
        result.append(right[0])
        right.pop(0)
    # SU SOLUCION TERMINA AQUI
    return result

def merge_sort(lista):
    if len(lista) == 1 :
        return lista

    mid = len(lista) // 2
    Listleft = lista[:mid]
    Listright = lista[mid:]
    left = merge_sort(Listleft)
    right = merge_sort(Listright)

    # SU SOLUCION TERMINA AQUI
    return merge(left, right)

print(merge_sort([8,12,1,3,5]))
# como funciona
"""
dividira la lista de forma entera en 2 listas
[8,12,1,3,5]
isquierda [8, 12]
derecha  [1,3,5] 

Izquierda
    vuelve a dividir la lista izquierda en 2
    [8] [12]
    las compara quien es meno y las vuelva a insertar en una nueva lista
    [8, 12]
Derecha
    vuelve a dividir entre 2 la lista de la derecha dando como resultado
    [1]
    [3,5]
    como aun queda una lista con mas de 1 elemento volvera a dividir teniendo como resultado
    [1][3][5]
    comparara  el y 3 y lo ordenara en una nueva lista
    [1 , 3 ]
    luego hara la comparacion  con el elmento 5 dando como resultado
    [1, 3, 5]
    
una vez vuelto a crear estas 2 listas se compararan y ordenaran en una nueva lista
[8, 12] y [1, 3, 5]
dando como resultado 
[1, 3, 5, 8 ,12]
    


"""
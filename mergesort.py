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

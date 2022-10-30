def shellsort(array):
    length = len(array)
    interval = length // 2
    while interval > 0:
        for i in range(interval, length):
            insert_value = array[i]
            insert_index = i
            
            while insert_index >= interval and array[insert_index - interval] > insert_value:
                array[insert_index] = array[insert_index - interval]
                insert_index -= interval
            
            array[insert_index] = insert_value
        interval //= 2
    return array

print(shellsort([8,12,1,3,5]))

# como funciona
"""
Como primera instancia tenemos nuestra lista
[8,12,1,3,5]
length = 5
interval = 2
la posicion 2(intervalo) se comparara con la posicion 0 y se remplazara si esta es menor que la posicion de caso contrario se mantendra ahi
[1,12,8,3,5]
luego se sumara una el intervalo haciendo que la comparacion sea entre la posicion 3 y la posicion 1
[1,3,8,12,5]
luego se sumara una el intervalo haciendo que la comparacion sea entre la posicion 4 y la posicion 2
[1,3,5,12,8]
luego el intervalo se volver a adividir entre 2 dando como resultado 1 
haciendo que la posicion 1 se compare con la posicion 0 y sera el mismo procedimiento
[1,3,5,12,8]   3 es > que 1 no se reemplaza
[1,3,5,12,8]   5 es > que 3 no se reemplaza
[1,3,5,12,8]   12 es > que 5 no se reemplaza
[1,3,5,12,8]   8 es < que 12 si se reemplaza dando como resultado
[1,3,5,8,12]
"""
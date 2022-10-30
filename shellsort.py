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

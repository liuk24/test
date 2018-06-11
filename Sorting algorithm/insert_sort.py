def insert_sort(array):
    for i in range(1,len(array)):
        min = array[i]
        j = i - 1
        while j >= 0 and array[j] > min:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = min
    return array
list=[9,8,2,0,6,5,7]
print(insert_sort(list))

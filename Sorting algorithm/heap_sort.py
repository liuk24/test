def sift(array,left,right):
    i = left
    j = 2*i + 1
    temp = array[i]
    while j <= right:
        if j < right and array[j] < array[j+1]:
            j = j + 1
        if temp < array[j]:
            array[i] = array[j]
            i = j
            j = 2*1 + 1
        else:
            break
    array[i] = temp


def heap(array):
    n = len(array)
    for i in range(n//2 - 1, -1, -1):
        sift(array, i, n-1)
    for i in range(n-1, -1, -1):
        array[0], array[i] = array[i], array[0]
        sift(array, 0, i-1)
    return array

list=[9,8,7,6,5,4,3,2,1]
print(heap(list))



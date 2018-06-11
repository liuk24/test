def shell_sort(array):
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, len(array)):
            tmp = array[i]
            j = i - gap
            while j >= 0 and tmp < array[j]:
                array[j + gap] = array[j]
                j -= gap
                array[j + gap] = tmp
        gap //= 2
    return array

list=[9,8,7,6,5,4,3,2,1]
print(shell_sort(list))
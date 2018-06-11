#直接选择排序  时间复杂度：O（n^2） 不稳定
def select_sort(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1,len(array)):
            if array[j] < array[min]:
                min = j
        array[i],array[min] = array[min],array[i]
    return array
list=[9,8,2,0,6,5,7]
print(select_sort(list))

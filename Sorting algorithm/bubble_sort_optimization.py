#冒泡排序（改进）  时间复杂度：O（n^2） 稳定
def bubble_sort(array):
    for i in range(len(array)-1):
        flag = False
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                flag = True
        if not flag:
            break
    return array
nums=[9,8,7,6,5,4,3,2,1]
print(bubble_sort(nums))
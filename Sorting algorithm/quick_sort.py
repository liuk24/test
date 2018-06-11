def quick_sort(array, left, right):
    if left < right:
        mid = partition(array, left, right)
        quick_sort(array, left, mid-1)
        quick_sort(array, mid+1, right)
    return array

def partition(array, left, right):
    temp = array(left)
    while left < right:
        while left < right and array[right] >= temp:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= tmp:
            left += 1
        array[right] = array[left]
    array[left] = temp
    return left


list=[9,8,7,6,5,4,3,2,1]
print(quick_sort(list))

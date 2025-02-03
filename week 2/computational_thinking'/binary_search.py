## determine if the target exist
import math


def binary_search(array, target, left, right):
    if left > right:
        return -1             # target not found
    
    mid = math.floor((left + right) / 2)

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, left, mid - 1)
    
    else:
        return binary_search(array, target, mid + 1, right)

'''
array = [0, 1, 2, 3, 4, 5]
target = 3
left = 0
right = 5

'''
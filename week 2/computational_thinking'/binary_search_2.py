## another binary search example

def binary_search(arr, target):
    left, right = (0, len(arr) - 1)

    while left <= right:

        mid = (left + right)//2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] <= target:
            left = mid + 1

        elif arr[mid] >= target:
            right = mid - 1

    return -1

print(binary_search(arr = [1, 3, 7, 9, 15, 43, 101, 135], target = 101))


'''
if __name__ == '_main_':
    arr = [1, 3, 7, 9, 15, 43, 101, 135]
    target = 101

    result= binary_search(arr, target)

    print(result)

    if result != 1: 
        print(result)

    else:
        print('Elemnt not found')
'''




## binary search using letters

def binary_leter_search(letters, target):
#    ord_array = []
#    target_numb = []

    left = 0 
    right = len(letters) - 1

    while left <= right:
        mid = (left + right) // 2
        letters[mid] = mid

        if mid > target:
            right = mid - 1
        
        elif mid < target:
            left = mid + 1

        else:
            return mid
            

letters = ['a', 'b', 'd', 'p', 'e', 'z', 'x', 'y']
letters = sorted(letters)
target = 'z'
print(binary_leter_search(letters, target))




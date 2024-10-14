inp = [1,2,3,13,25,123]

## target is 2

def binary_search(arr, target):
    left = 0 ## 0 -> 1
    right = len(arr) - 1 ## 5 > 1

    while left <= right:
        mid = (left + right) // 2 ## 1

        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return mid
    
    return -1

print(binary_search(inp, 13))
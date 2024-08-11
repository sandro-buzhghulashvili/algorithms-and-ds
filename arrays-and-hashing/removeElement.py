## Input: nums = [3,2,2,3], val = 3

def removeElement(arr, value):
    k = 0 ## number of values that are not equal to input value
    for i in range(0, len(arr)):
        if arr[i] != value:
            arr[k] = arr[i]
            k += 1
    for i in range(k, len(arr)):
        arr[i] = '_'
    
    return arr, k

print(removeElement([1,2,5,4,2,3,1], 2))

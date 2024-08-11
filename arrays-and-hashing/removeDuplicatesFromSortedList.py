## Input: nums = [1,1,2,2,3]

def removeDuplicates(arr):
    k = 1 ## number of unique elements
    for i in range(1, len(arr)):
        if arr[i] != arr[k - 1]: ## if number is unique move, otherwise increment k and swap it with k-th index item which is not duplicate
            arr[k] = arr[i]
            k+=1
    for i in range(k, len(arr)):
        arr[i] = "_"

    return k, arr


print(removeDuplicates([1,1,2,2,3]))
    

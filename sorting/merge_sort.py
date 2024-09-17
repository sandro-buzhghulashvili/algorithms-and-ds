inp = [5,2,3,1]

def mergeSortedArrays(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m + 1: r + 1]

    i = l # pointer to main array
    j = 0 # pointer to left half
    k = 0 # pointer to right half

    while j < len(left) and k < len(right):
        if left[j] < right[k]:
            arr[i] = left[j]
            j += 1
        else :
            arr[i] = right[k]
            k += 1
        i += 1

    while j < len(left):
        arr[i] = left[j]
        j+=1
        i+=1
    while k < len(right):
        arr[i] = right[k]
        k+=1
        i+=1    



def mergeSort(arr, l, r):
    if l == r : return None

    mid_point = (l + r) // 2

    mergeSort(arr, l, mid_point)
    mergeSort(arr, mid_point + 1, r)

    mergeSortedArrays(arr, l, mid_point, r)


mergeSort(inp, 0, len(inp) - 1)
print(inp)
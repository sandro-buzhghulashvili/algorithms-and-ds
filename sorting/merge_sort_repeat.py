## input : [1,5,2,3]

inp = [1,5,2,3,1,4,5,2.3,13,12,11]

def merge(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]

    i, j, k  = l, 0, 0

    while j < len(left) and k < len(right):
        if left[j] < right[k]:
            arr[i] = left[j]
            j+=1
        else:
            arr[i] = right[k]
            k+=1
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
    if l == r: return

    mid_point = (l + r) // 2

    mergeSort(arr, l, mid_point)
    mergeSort(arr, mid_point + 1, r) 

    merge(arr, l, mid_point, r )

mergeSort(inp, 0, len(inp) - 1)

print(inp)
inp = [2,5,1,3]

def quick_sort(arr, s, e):
    if s >= e: return 

    pivot = arr[e]
    j = s

    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp
            j+=1
    
    arr[e] = arr[j]
    arr[j] = pivot

    quick_sort(arr, s, j - 1)
    quick_sort(arr, j + 1, e)

quick_sort(inp, 0, 3)

print(inp)
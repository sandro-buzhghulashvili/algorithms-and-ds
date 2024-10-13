inp = [1,5,0.5,3, 7, 6.2,-5,9,9,0] 

def quick_sort(arr, s, e):
    if e <= s: return

    pivot = arr[e]
    j = s

    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp
            j+=1

    arr[e] = arr[j] ## [1,5,0.5,3] -> [1, 0.5, 3, 5, 4]
    arr[j] = pivot

    quick_sort(arr, s, j - 1)
    quick_sort(arr, j + 1, e)
    
quick_sort(inp, 0, len(inp) - 1)
print(inp)
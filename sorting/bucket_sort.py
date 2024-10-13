inp  = [1,0,0,1,1,2,1,0]


def bucket_sort(arr):
    counts = [0, 0, 0]
    for i in arr:
        counts[i] += 1
    i = 0
    for j in range(0, len(counts)):
        for k in range(0, counts[j]):
            arr[i] = j
            i+=1
    

bucket_sort(inp)
print(inp)
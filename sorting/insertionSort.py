
inp = [3, 1, 0, 2, 5]

def sort(arr):
    for i in range(1, len(arr)):
        cur = arr[i] # 0
        prev = i - 1 # 1 -> 0

        while prev >= 0 and cur < arr[prev]:
            arr[prev + 1] = arr[prev]
            prev -= 1

        arr[prev + 1] = cur

sort(inp)
print(inp)
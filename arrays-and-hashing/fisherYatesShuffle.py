import random
## [1,2,3,4]

def shuffle(arr):
    n = len(arr)

    while n > 0:
        random_index = random.randint(0, n - 1)
        tmp = arr[random_index]
        arr[random_index] = arr[n - 1]
        arr[n - 1] = tmp
        n-=1

input_array = [1,2,3,4]
shuffle(input_array)
print(input_array)
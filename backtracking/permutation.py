inp = [1,2]

def permutation(arr):
    res = []
    
    def backtrack(start):
        if start == len(arr):
            res.append(arr.copy()) 
            return
        
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1)
            arr[start], arr[i] = arr[i], arr[start] 

    backtrack(0)
    return res


print(permutation(inp))

        
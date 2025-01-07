inp = [2,5,3,1]
target = 13

def combinationSum(arr, target):
    res = []

    def dfs(index, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if total > target or index == len(arr):
            return 
        
        cur.append(arr[index])
        dfs(index, cur, total + arr[index])

        cur.pop()
        dfs(index + 1, cur, total)
    
    dfs(0, [], 0)
    return res

print(combinationSum(inp, target))
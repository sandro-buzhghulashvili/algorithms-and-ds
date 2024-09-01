def numberOfPartitionsWithMaxPart(n, max_part):
    dp = [0] * (n + 1)
    
    dp[0] = 1
    
    for i in range(1, max_part + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    
    return dp[n]

n = 100
max_part = 50
print(numberOfPartitionsWithMaxPart(n, max_part))  

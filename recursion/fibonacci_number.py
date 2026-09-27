def fib(self, n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    return self.fib(n - 1) + self.fib(n - 2)

def fib_iterative(n):
    first_num = 0
    second_num = 1

    for i in range(2, n + 1):
        sum_num = first_num + second_num
        first_num = second_num
        second_num = sum_num
    
    return second_num

print(fib_iterative(100))

## Memoizing approach


class Solution:
    def __init__(self):
        self.cache = {
            0 : 0,
            1 : 1
        }
    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]            
        
        res = self.fib(n - 1) + self.fib(n - 2)
        self.cache[n] = res
        
        return res
        

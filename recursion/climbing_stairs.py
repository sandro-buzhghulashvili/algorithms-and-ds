class Solution:
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n: int) -> int:
        if n == 2: return 2
        if n == 1: return 1

        if n in self.memo:
            return self.memo[n]

        res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n] = res

        return res

## new approach (basically same as previous one):
class Solution:
    def __init__(self):
        self.cache = {
            1 : 1,
            2 : 2
        }
    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.cache[n] = res
        return res
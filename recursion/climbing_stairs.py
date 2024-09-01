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
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        x = []
        def backtrack(iteration):
            if iteration >= len(nums):
                res.append(x.copy())
                return
            
            x.append(nums[iteration])
            backtrack(iteration + 1)

            x.pop()
            backtrack(iteration + 1)
        
        backtrack(0)
        return res
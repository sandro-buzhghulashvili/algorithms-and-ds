## Input: nums = [2,5,1,3,4,7], n = 3

from typing import List


def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(0, n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res

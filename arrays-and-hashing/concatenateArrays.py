from typing import List


def getConcatenation(self, nums: List[int]) -> List[int]:
        concatenated = []
        for i in range(0, 2):
            for num in nums:
                concatenated.append(num)
        
        return concatenated
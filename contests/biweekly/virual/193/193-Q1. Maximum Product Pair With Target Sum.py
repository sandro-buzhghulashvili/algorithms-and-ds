
test = [0,7,8,1,-1,-2,-12]
print(0 == 0)

def maxProductPair(nums: list[int], target: int) -> list[int]:
        valid_options = {}

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if (nums[i] + nums[j] == target):
                        if(nums[i] > nums[j]):
                            valid_options[(i, j)] = nums[i] * nums[j]
                        if(nums[j] > nums[i]):
                            valid_options[(j, i)] = nums[i] * nums[j]

        print(valid_options)
        maxVal = None
        maxPair = (-1, -1)
        for opt in valid_options:
            if maxVal != 0 and not maxVal:
                maxVal = valid_options[opt]
                maxPair = opt
            else:
                if(valid_options[opt] > maxVal):
                    maxVal = valid_options[opt]
                    maxPair = opt
             
        return list(maxPair)

print(maxProductPair(test, -1))
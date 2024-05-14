# my solution - O(n^2):

# def productExceptSelf(self, nums):
#         res = [0 for i in range(len(nums))]

#         for numIndex in range(len(nums)):

#             left_product = 1
#             for j in range(numIndex - 1, -1, -1):
#                 left_product = left_product * nums[j]

#             right_product = 1
#             for k in range(numIndex + 1, len(nums)):
#                 right_product = right_product * nums[k]
            
#             res[numIndex] = left_product * right_product

#         return res

# my second solution after watching whiteboard explanation - O(n):
def productExceptSelf(self, nums):
        res = [1] * len(nums)

        post_fix = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                post_fix[i] = nums[i]
            else:
                post_fix[i] = post_fix[i - 1] * nums[i]

        pre_fix = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == (len(nums) - 1):
                pre_fix[i] = nums[i]
            else:
                pre_fix[i] = pre_fix[i + 1] * nums[i]            

        for i in range(len(nums)):
            if i == 0:
                res[i] = pre_fix[i + 1]
            elif i == len(nums) - 1:
                res[i] = post_fix[i - 1]
            else:
                res[i] = post_fix[i - 1] * pre_fix[i + 1]

        
        return res

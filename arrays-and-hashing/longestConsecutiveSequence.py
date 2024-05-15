# Input: nums = [100,4,200,1,3,2]

# my solution - O(n): 

# def longestConsecutive(nums):
#     numsSet = set(nums)
#     frequencies = []

#     for num in nums:
#         if (num - 1) not in numsSet:
#             temp_num = num
#             frequency = [temp_num]
#             while (temp_num + 1) in numsSet:
#                 frequency.append(temp_num + 1)
#                 temp_num += 1
#             frequencies.append(frequency)
    
#     longestFrequency = 0
#     for f in frequencies:
#         if len(f) > longestFrequency:
#             longestFrequency = len(f)
    
#     return longestFrequency

# longestConsecutive([100,4,200,1,3,2])

# neetcode solution - O(n) :

def longestConsecutive(nums):
    numsSet = set(nums)
    longest = 0

    for i in nums:
        if (i - 1) not in numsSet:
            length = 0
            while (i + length) in numsSet:
                length+=1
            if length > longest:
                longest = length
    
    return longest

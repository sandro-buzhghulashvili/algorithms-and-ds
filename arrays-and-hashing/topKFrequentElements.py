# my solution O(n + k)

# def topKFrequent(self, nums, k):
#         hashMap = {}

#         for num in nums:
#             if num in hashMap:
#                 hashMap[num] += 1
#             else :
#                 hashMap[num] = 1
        
#         bucket = [0] * (len(nums) + 1)

#         for item in hashMap.items():
#             if bucket[item[1]] != 0:
#                 bucket[item[1]].append(item[0])
#             else:
#                 bucket[item[1]] = [item[0]]

#         res = []
        
#         for i in range(len(bucket) - 1,0, -1):
#             if len(res) == k : break
#             if bucket[i] != 0:
#                 res.extend(bucket[i])
        
#         return res

# neetcode soluton: O(n) - linear time complexity

def topkFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if(len(res) == k):
                return res
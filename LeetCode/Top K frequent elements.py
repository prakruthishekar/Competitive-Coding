# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

from collections import Counter
def topKFrequent(nums, k: int):
        d = {}

        for i in range(len(nums)):
            if(nums[i] not in d):
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1 

        value = dict(sorted(d.items(),key=lambda x: x[1], reverse=True))
        result = list(value.keys())[:k]
        return list(result) 


# def topKFrequent(nums, k: int):
        # freq_table = Counter(nums)
        # ans_table = freq_table.most_common()
        # ans = []
        # for key, _ in ans_table:
        #     if k <= 0:
        #         break
        #     k -= 1
        #     ans.append(key)
        # return ans

print(topKFrequent([1,1,1,2,2,3],2))

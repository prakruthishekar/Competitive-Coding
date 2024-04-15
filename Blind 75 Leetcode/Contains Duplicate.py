# class Solution(object):
#         def containsDuplicate(self, nums):
#             freq = {}
#             for i,num in enumerate(nums):
#                 if(num not in freq):
#                     freq[num] = i
#                 else:
#                     return True
#             return False  


class Solution:
    def containsDuplicate(self, nums) -> bool:
        return not(sorted(nums) == sorted(set(nums)))





nums = [3,3]
classObject = Solution() 
print(classObject.containsDuplicate(nums))         



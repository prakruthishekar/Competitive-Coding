# Given an array nums of n integers where nums[i] is in the range [1, n], return an 
# array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]


# class Solution:
#     def findDisappearedNumbers(self, nums):
#         print(set(nums))
#         print(range(1,len(nums)+1))
#         print(set(range(1,len(nums)+1)))
#         return set(range(1, len(nums)+1)) - set(nums)


class Solution:
    def findDisappearedNumbers(self, nums):
        for i in nums:
            # print(abs(i)-1)
            nums[abs(i)-1]  = -abs(nums[abs(i)-1])
            
        return [i+1 for i in range(len(nums)) if nums[i] > 0]       



# Time complexity : O(n)
# Space complexity : O(1)       

classObject = Solution()

print("the missing number in the range: ", classObject.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print("the missing number in the range: ", classObject.findDisappearedNumbers([1,1]))      
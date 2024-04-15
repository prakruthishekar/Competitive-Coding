# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2



def majorityElement(nums):
        curr, count = nums[0], 1    # curr will store the current majority element, 
        # count will store the count of the majority
        for i in nums[1:]:
            count += (1 if curr == i else -1) # if i is equal to current majority, they're in same team,
            #  hence added, else one current majority and i both will be dead
            if not count:           # if count of current majority is zero, then change the majority
                #  element, and start its count from 1
                curr = i
                count = 1
        return curr
# def majorityElement(nums) -> int:
#     return sorted(nums)[len(nums) // 2]


print(majorityElement([1,3,3,3,1,1,1,3,32,1,1]))        
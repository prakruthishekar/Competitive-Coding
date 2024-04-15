# Given a list of non-negative integers nums, arrange them such that they
# form the largest number and return it.

# Since the result may be very large, so you need to return a string 
# instead of an integer.

 

# Example 1:

# Input: nums = [10,2]
# Output: "210"
# Example 2:

# Input: nums = [3,30,34,5,9]
# Output: "9534330"


def largestNumber(nums):
    nums = [str(num) for num in nums]
    nums.sort(key=lambda x: x*10**10, reverse=True)  # Sort by comparing x*10^10 to ensure proper string concatenation
    largest_num = ''.join(nums)

    if largest_num[0] == '0':
        return '0'

    return largest_num




print(largestNumber([3,30,34,5,9]))
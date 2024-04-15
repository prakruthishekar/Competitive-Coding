# Given an unsorted array containing numbers and a number ‘k’,
# find the first ‘k’ missing positive numbers in the array.

# Example 1:

# Input: [3, -1, 4, 5, 5], k=3
# Output: [1, 2, 6]
# Explanation: The smallest missing positive numbers are 1, 2 and 6.
# Example 2:

# Input: [2, 3, 4], k=3
# Output: [1, 5, 6]
# Explanation: The smallest missing positive numbers are 1, 5 and 6.
# Example 3:

# Input: [-2, -3, 4], k=2
# Output: [1, 2]
# Explanation: The smallest missing positive numbers are 1 and 2.


def findKthPositive(nums, k: int) -> int:
    i = 0
    n = len(nums)
    while(i < len(nums)):
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i+= 1

    missing_number = []
    extra_numbers = []
    for i in range(len(nums)):
        if len(missing_number)< k:
            if nums[i] != i+1:
                missing_number.append(i+1)
                extra_numbers.append(nums[i])

    # add the reamining missing numbers
    i = 1
    while len(missing_number) < k:
        candidate_number = i + n  
          #ignore the array if it contains the candidate number
        if candidate_number not in extra_numbers:
            missing_number.append(candidate_number)
        i += 1 
    return missing_number[-1]
    
print(findKthPositive([2,3,4,7,11], 5))
print(findKthPositive([2, 3, 4], 3))
print(findKthPositive([-2, -3, 4], 2))
print(findKthPositive([5,6,7,8,9],9))

# We are given an unsorted array containing numbers taken from 
# the range 1 to ‘n’. The array can have duplicates, which means 
# some numbers will be missing. Find all those missing numbers.

# Example 1:

# Input: [2, 3, 1, 8, 2, 3, 5, 1]
# Output: 4, 6, 7
# Explanation: The array should have all numbers from 1 to 8, due to 
# duplicates 4, 6, and 7 are missing.
# Example 2:

# Input: [2, 4, 1, 2]
# Output: 3
# Example 3:

# Input: [2, 3, 2, 1]
# Output: 4






# def find_all_missing_numbers(nums):
#         for i in nums:
#             nums[abs(i)-1]  = -abs(nums[abs(i)-1])
            
#         return [i+1 for i in range(len(nums)) if nums[i] > 0]


def find_all_missing_numbers(nums):
    i = 0
    while(i< len(nums)): 
        # print(num[i])  
        j = nums[i] - 1 # find the correct index the value suppoe to go
        if(nums[i] != nums[j]):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        else:
            i += 1    
    missing_numbers = []

    for i in range(len(nums)):
        if nums[i] != i+1:
            missing_numbers.append(i+1)  
    
    return missing_numbers


print(find_all_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))   

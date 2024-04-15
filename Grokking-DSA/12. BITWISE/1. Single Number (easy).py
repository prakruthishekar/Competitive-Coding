# Problem Statement #
# In a non-empty array of integers, every number appears twice except for one,
#  find that single number.

# Example 1:

# Input: 1, 4, 2, 1, 3, 2, 3
# Output: 4



def single_number(num):

    result = num[0]
    
    for i in range (1,len(num)):

        result ^= num[i]
    return result    




print(single_number([1, 4, 2, 1, 3, 2, 3]))
print(single_number([7, 9, 7]))    

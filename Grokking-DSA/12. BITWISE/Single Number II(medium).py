# Given an integer array nums where every element appears three times except for one, 
# which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99



### Hashing:

# def single(nums):
#         d = {}
#         for i in nums:
#             if i in d:
#                 d[i] += 1
#             else:
#                 d[i] = 1
#         for a,b in d.items():
#             # print(a,b)
#             if b == 1:
#                 return a




## Array Sum
# def single(nums):
#         a = 3*sum(set(list(nums))) - sum(nums) 
#         return (a)//2  



## Sorting and linear traversal

def single(nums):
    nums.sort() 
    if(nums[0] != nums[1]): # Edge case
        return nums[0]

    if(nums[len(nums)-1] != nums[len(nums)-2]): # Edge case
        return nums[len(nums)-1]
    
    for i in range(1,len(nums),3):  
        if(nums[i-1] == nums[i]):
            continue
        return nums[i-1]
    return [0]    

print(single([2,2,3,2]))
print(single([0,1,0,1,0,1,99,101,101,101]))    

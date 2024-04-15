# We are given an unsorted array containing ‘n’ numbers taken 
# from the range 1 to ‘n’. The array has some duplicates, 
# find all the duplicate numbers without using any extra space.

# Example 1:

# Input: [3, 4, 4, 5, 5]
# Output: [4, 5]
# Example 2:

# Input: [5, 4, 7, 2, 3, 5, 3]
# Output: [3, 5]



# def find_duplicates(nums):
#         A = []
#         for n in nums:
#             if nums[abs(n)-1] > 0: 
#                 nums[abs(n)-1] = -nums[abs(n)-1]
#             else: A.append(abs(n))
#         return A



def find_duplicates(nums):
    i = 0
    duplicates = []
    while(i < len(nums)):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
         if nums[i] != i+1:# we have found the duplicate
            duplicates.append(nums[i])
            i += 1
    print(nums)          
    return duplicates

# print(find_duplicates([3, 4, 4, 5, 5]))
# print(find_duplicates([5, 4, 7, 2, 3, 5, 3]))



def find_duplicates(nums):
    duplicates = []
    for n in nums:
        if nums[abs(n)-1] > 0:
            nums[abs(n)-1] = -nums[abs(n)-1]
        else:
            duplicates.append(abs(n))
    
    for i in range(len(nums)):
        if nums[i]<0:
            nums[i] *= -1
    print(nums)
    return duplicates

print(find_duplicates([3, 4, 4, 5, 5]))

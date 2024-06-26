# We are given an unsorted array containing ‘n+1’ numbers taken from the
# range 1 to ‘n’. The array has only one duplicate but it can be repeated 
# multiple times. Find that duplicate number without using any extra space. 
# You are, however, allowed to modify the input array.

# Example 1:

# Input: [1, 4, 4, 3, 2]
# Output: 4
# Example 2:

# Input: [2, 1, 3, 3, 5, 4]
# Output: 3
# Example 3:

# Input: [2, 4, 1, 4, 4]
# Output: 4



def find_duplicates(nums):
    i = 0
    while(i < len(nums)):
        if nums[i] != i+1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else: # we have found the duplicate
                return nums[i]
        
        else:
            i += 1


            #Using Binary search
def find_duplicates(nums) -> int:
        nums.sort()
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] < mid+1:
                r = mid - 1
            else:
                l = mid + 1
        return l  

print(find_duplicates([1, 4, 4, 3, 2]))
print(find_duplicates([2, 1, 3, 3, 5, 4]))
print(find_duplicates([2, 4, 1, 4, 4]))
print(find_duplicates([1,2,3,4,5,6,6]))


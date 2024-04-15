# Given an array of numbers which is sorted in ascending order and
# is rotated ‘k’ times around a pivot, find ‘k’.

# You can assume that the array does not have any duplicates.

# Example 1:

# Input: [10, 15, 1, 3, 8]
# Output: 2
# Explanation: The array has been rotated 2 times.
 
# Example 2:

# Input: [4, 5, 7, 9, 10, -1, 2]
# Output: 5
# Explanation: The array has been rotated 5 times.



def count_rotation(arr):
    start, end = 0, len(arr) - 1

    while( start < end):
        mid = (start + end) // 2

        #if mid is greater than the next element
        if mid < end and arr[mid] > arr[mid+1]:
            return mid + 1
        

        # if mid is smaller than the previous element
        if mid > start and arr[mid-1] > arr[mid]:
            return mid
        
        # left side is sorted so pivot is on the right side
        if arr[start] < arr[mid]:
            start = mid + 1
        else: # right side is sorted so pivot is on the left side
            end = mid - 1
    
    return 0 # the array has not been rotated



print(count_rotation([10, 15, 1, 3, 8]))
print(count_rotation([4, 5, 7, 9, 10, -1, 2]))

